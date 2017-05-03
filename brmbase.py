#!/usr/bin/python2.7
# -*- encoding:utf8 -*-

import random

debug = 0

def main():
    b = brmbase(talent=['black','light','ht','bc','ed'],equip=['ring','waist','wrist'], \
            iron = 8, palmcdr = 1.4, haste = 1.3, dodgebase = 0.08, mastery = 0, crit = 0, vers = 0 )

    print brmbase.__dict__

    class test(brmbase):
        def run(this):
            print 'hello'
            print this.__dict__

    t = test()
    t.run()


class Event:
    time = 0
    dst = 0
    src = 0
    el = 0

    def addto(this, el):
        el.add(this)

    def __init__(this, src = 0, time=0, dst = 0):
        this.time = time
        this.src = src
        this.dst = dst
    def __repr__(this):
        return this.__class__.__name__+" at %.3f"%this.time
    def __str__(this):
        return this.__class__.__name__+" at %.3f"%this.time

    def move(this, offset = 0, newtiming = 0):
        this.el.move(this, offset, newtiming)

    def rm(this):
        this.el.rm(this)

    def elprocess(this):
        this.process()

    def process(this):
        print this.time,'process'
#}

class RepeatEvent(Event):
    repeat = 0

    def __init__(this, src, repeat = 1,time=0, dst=0):
        Event.__init__(this, src, time, dst)
        #if this.repeat != 0 :
        this.repeat = repeat

    def repeatproc(this):
        print this.time,this,'repeatproc (deprecated)'

    def elprocess(this):
        this.process()
        if this.repeat == 0 :
            return
        this.time += this.repeat
        this.el.add(this)

    def process(this):
        print this.time,'repeatev proc'


#}class repeatevent



class Eventlist:
    time = 0
    _list = []
    brm = 0
    def __str__(this):
        return str(this._list)

    def __init__(this):
        this._list = []


    def add(this,event):
        event.el = this
        if debug == 1:
            print "%.3f"%this.time,'add',event
        timing = event.time
        for i in range(len(this._list)) :
            if timing <= this._list[i].time  :
                tmp = this._list[:i]
                tmp.append(event)
                tmp += this._list[i:]
                this._list = tmp
                return True
        this._list.append(event)
    #}
    
    def rm(this,event):
        for i in range(len(this._list)) :
            if this._list[i] == event :
                ret = this._list.pop(i)
                event.el = 0
                return ret
        print this.time, ': rm 404', event
        print this
        exit()
        return 0


    def move(this, event, offset = -1, newtiming = 0):
        if newtiming == 0:
            e = this.rm(event)
            if e == 0 :
                print this.time,': move 404', event
                return 
            e.time += offset
           # if e.time < this.time :
           #     e.time = this.time
            this.add(e)
        else :
           # if newtiming < this.time :
           #     newtiming = this.time
            e = this.rm(event)
            if e == 0 :
                print this.time,': move 404', event
                return 
            e.time = newtiming
            this.add(e)


    def procone(this):
        e = this._list.pop(0)
        if debug == 1:
            print e,this._list
        if this.time < e.time:
            this.time = e.time
        if debug == 1:
            print '%.2f: '%this.time,e,this
        e.elprocess()
        return #this.time
    

    def run(this, time = 10000):
        while(1):
            if this.time > time :
                return
            this.procone()

#} class eventlist

class config():
    count = [0]
    def show(this):
        print this.stat,this.equip,this.talent,this.iduration,this.palmcdr

    def __init__(this,stat=0,equip=['4t'],talent=['black','ht15'],iduration=8.5, prate = 0.5,palmcdr=1.4, haste=0, crit=0, vers=0, mastery=0):
        if stat == 0 :
            stat = [25,25,0,27]
        if len(stat)!= 4:
            print 'stat err'
            exit()
        this.stat = stat
        this.crit = float(stat[0])/100
        this.haste = float(stat[1])/100+1
        this.vers = float(stat[2])/100
        this.mastery = float(stat[3])/100
        this.equip = equip
        this.talent = talent
        this.iduration = iduration
        this.palmcdr = palmcdr
        this.prate = prate

        if crit != 0 :
            this.crit = crit
            this.stat[0] = int(crit*100)
        if haste != 0 :
            this.haste = haste
            this.stat[1] = int(haste*100-100)
        if vers != 0 :
            this.vers = vers
            this.stat[2] = int(vers*100)
        if mastery != 0 :
            this.mastery = mastery
            this.stat[3] = int(mastery*100)

    haste = 0
    crit = 0
    mastery = 0
    vers = 0
    stat = []

    palmcdr = 0
    iduration = 0
    prate = 0

    equip=[]
    talent=[]


class brmbase:
    #ed : elusive dance
    #ht : high tolerance
    #bc : blackout combo


    fout = 0

    el = 0

    talent = []
    equip = []
    stat = []
    conf = 0

    ring = 0
    waist = 0
    wrist = 0

    #stat
    dodgebase = 0.08
    mastery = 0.3
    masterystack = 0
    meleecount = 0
    dodgecount = 0
    haste = 1.3
    crit = 0.1
    vers = 0

    iduration = 8
    kegcdr = 4
    palmcdr = 1.4
    brewcd = 21
    brewstack = 3
    brewstackmax = 3


    #stagger
    ironskin = 1
    prate = 0.5 # purify rate
    phrate = 0  # purify healrate
    srate = 0.4 # stagger rate
    irate = 0.75 # stagger rate (ironskin)
    stdmgrate = 1.0/20 # stagger dmg rate
    st = 0  # stagger pool
    sttick = 0 # stagger tick

    #statis
    dtb4st = 0 # total dmg taken
    stout = 0 # st avoidance
    totaltank = 0
    sttaken = 0
    stin = 0
    pbpury = 0
    puryheal = 0
    facetaken = 0

    def takephydmg(this,dmg=100,rate=0.9):
        if this.ironskin == 1 :
            rate = this.irate
        else :
            rate = this.srate
        this.dtb4st += dmg
        this.stin += rate * dmg
        this.facetaken += dmg * (1-rate)
        this.st += rate * dmg
        this.sttick = this.st * this.stdmgrate

    def takemelee(this,dmg=100,rate=0.9):
        this.totaltank += 0
        if this.mastery == 0:
            this.takephydmg(dmg)
        else :
            r = random.random()
            dodge = this.dodgebase + this.mastery* this.masterystack
            if r < dodge:
                this.masterystack = 0
            else:
                this.takephydmg(dmg)
                this.masterystack += 1
   #}takemelee

    def takestdmg(this):
        if this.st <= 0 :
            return

        this.sttaken += this.sttick
        this.st -= this.sttick

    def pury(this):
        this.stout += this.prate * this.st 
        this.pbpury += this.prate * this.st 
        if this.crit != 0 :
            this.puryheal += this.phrate * this.st * ( 1 + this.crit * 0.65 )
        else :
            this.puryheal += this.phrate * this.st

        this.st -= this.prate * this.st
        this.sttick -= this.sttick * this.prate

    def showavoid(this):
        print 'stat\t',this.stat
        print 'talent\t',this.talent
        print 'equip\t',this.equip
#        if this.prate == 0.65:
#            print 'ed',  
#        elif this.srate == 0.5:
#            print 'ht',
#        else :
#            print 'bc',
#        if this.ring == 1 :
#            print 'ring',
#        if this.waist ==1:
#            print 'waist',
#        if this.wrist ==1:
#            print 'wrist'
#
        avoidance = this.getehrr()
        print '----------------------------'
        print ' ehr ->| %.4f%% |<- reduced'%(avoidance*100)
        print '----------------------------'
        print 'totalmeleetank', this.totaltank
        print 'dmgtaken b4st',this.dtb4st
        print 'stagger input', this.stin
        print 'stagger taken', this.sttaken
        print 'stagger purified %d(%.2f%%)'%(this.stout,this.stout/this.stin*100)
        print 'purifybrew purified %d(%.2f%%)'%(this.pbpury,this.pbpury/this.stin*100)
        if this.phrate != 0 :
            print 'waist heal',this.puryheal
        if this.mastery != 0 and this.dodgecount!= 0:
            print "dodge count %d(%.2f%%)"%(this.dodgecount, float(this.dodgecount)*100/this.meleecount)
        return avoidance

    def getavoid(this):
        return (this.stout + this.puryheal) / this.dtb4st

    def getehr(this):
        return 1/(1-this.stout - this.puryheal/this.dtb4st)

    def getehrr(this):
        return 1-this.getehr()

    def iron(this,time = 1):
        for i in range(time):
            this.takephydmg(this.irate)
            this.takestdmg()
            this.takestdmg()


    def __init__(this,conf=0,talent=['black','ht'],equip=['ring','waist'], \
            iduration = 8, prate=0.5, palmcdr = 1.4, haste = 1.3, dodgebase = 0.10, mastery = 0, crit = 0, vers = 0 ):
        random.seed(1)


        this.el = Eventlist()
        this.el.brm = this

        if conf == 0 :
            tmpstat = [int(crit*100),int(haste*100-100),int(vers*100),int(mastery*100)]
            conf = config(stat=tmpstat, equip = equip, talent = talent, palmcdr = palmcdr, iduration = iduration, prate = prate)

        this.conf = conf

        this.dodgebase = dodgebase
        this.kegcdr = 4

        this.iduration = conf.iduration
        this.prate = conf.prate
        this.mastery = conf.mastery
        this.haste = conf.haste
        this.crit = conf.crit
        this.vers = conf.vers
        this.palmcdr = conf.palmcdr
        this.talent = conf.talent
        this.equip = conf.equip
        this.stat = conf.stat


        for t in this.talent:
            if t == 'ht' or t == 'ht1' or t == 'ht10':
                this.srate = 0.5
                this.irate = 0.9
                this.haste *= 1.1
            elif t == 'ht15':
                this.srate = 0.5
                this.irate = 0.9
                this.haste *= 1.15
            elif t == 'ed' or t == 'ed13' or t == 'ed20':
                this.prate += 0.15
            elif t == 'ednobuff' :
                this.prate += 0.15
            elif t == 'bc':
                this.kegcdr = 6
            elif t == 'light':
                this.brewcd = 18
                this.brewstack = 4
                this.brewstackmax = 4
            
        for e in this.equip:
            if e == '2t' :
                this.irate += 0.05
                this.srate += 0.05
            if e == '4t' :
                this.irate += 0.05
                this.srate += 0.05
                this.palmcdr += 1
            if e == 'ring':
                this.ring =1
                this.stdmgrate = 1.0/26
            if e == 'waist':
                this.waist =1
                this.phrate = this.prate * 0.25
            if e == 'wrist':
                this.wrist =1

        this.brewcd /= this.haste


    #}init
#}class brmbase



if __name__ == '__main__' :
    main()
