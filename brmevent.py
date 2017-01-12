#!/usr/bin/python2.7
# -*- encoding:utf8 -*-

import random

class Event:
    me = 0
    clock = 0
    def __init__(this, brm = 0, clock = 0):
        this.clock = clock
        this.me = brm
    def __repr__(this):
        return "event at %.1f"%this.clock
    def __str__(this):
        return "event at %.1f"%this.clock

    def process(this):
        print 'process me at %.1f'%this.clock
#}

class Eventlist:
    clock = 0
    _list = []

    def add(this,event):
        timing = event.clock
        for i in range(len(this._list)) :
            if timing <= this._list[i].clock  :
                tmp = this._list[:i]
                tmp.append(event)
                tmp += this._list[i:]
                this._list = tmp
                #print this._list
                return True
        this._list.append(event)
    #}

    def procone(this):
        e = this._list.pop(0)
        e.process()
        this.clock = e.clock
        return #this.clock
    
    def run(this, time = 10000):
        while(1):
            if this.clock > time :
                return
            this.procone()

#} class eventlist

def main():
    el = Eventlist()
    b = brm()

    class Stevent(Event):
        def process(this):
            this.me.takestdmg()
            this.clock += 0.5
            print this.me.st
            el.add(this)
    
    class Meleeevent(Event):
        def process(this, iv = 1.5):
            this.me.takemelee()
            this.clock += iv
            el.add(this)

    class Puryevent(Event):
        def process(this, iv = 15):
            this.me.pury()
            this.clock += iv
            el.add(this)
            

    e = Stevent(b)
    el.add(e)

    e = Meleeevent(b)
    el.add(e)

    e = Puryevent(b)
    el.add(e)

    el.run(20)
    b.showavoid()



class brm:
    #ed : elusive dance
    #ht : high tolerance
    #bc : blackout combo

    def ah(this):
        print 'ah'
    fout = 0
    clock = 0

    t3 = ''
    t7 = ''
    light = 0

    ring = 0
    waist = 0
    wrist = 0

    dodgebase = 0.08
    mastery = 0.3
    haste = 1.3

    iduration = 7.5
    palm = 1.3

    prate = 0.5 # purify rate
    phrate = 0  # purify healrate
    srate = 0.4 # stagger rate
    irate = 0.8 # stagger rate (ironskin)
    stdmgrate = 1.0/20 # stagger dmg rate

    st = 0  # stagger pool
    sttick = 0 # stagger tick

    total = 0 # total dmg taken
    avoid = 0 # avoidance
    facetotal = 0
    sttaken = 0
    stin = 0

    class Cd():
        clock = 0
        cd = 0
        stack = 1
        stackmax = 1

        def __init__ (this, cd, stack=1):
            this.cd = cd
            this.stackmax = stack
            this.stack = stack

        def cool(this,offset):
            this.clock += offset
            if this.clock > this.cd :
                this.stack += 1
                if this.stack > this.stackmax :
                    this.stack = this.stackmax
            if this.stack == this.stackmax :
                this.clock = 0

        def remain(this):
            return cd - clock




    def takestdmg(this):
        if this.st <= 0 :
            return

        this.sttaken += this.sttick
        this.st -= this.sttick

    def pury(this):
        this.avoid += (this.phrate + this.prate) * this.st 
        this.st -= this.prate * this.st
        this.sttick -= this.sttick * this.prate

    def takemelee(this):

        rate = 0.9

        if this.mastery == 0:
            this.total += 100.0
            this.stin += rate * 100
            this.st += rate * 100
            this.sttick = this.st * this.stdmgrate
        else :
            r = random.random()
            dodge = this.dodgebase + this.mastery* this.masterystack
            if r < dodge:
                this.masterystack = 0
                if this.wrist == 1:
                    this.puryclock+=1
                return
            else:
                this.total += 100.0
                this.st += rate * 100
                this.sttick = this.st * this.stdmgrate
                this.masterystack += 1
#   }

    def showavoid(this):
        if this.prate == 0.65:
            print 'ed',  
        elif this.srate == 0.5:
            print 'ht',
        else :
            print 'bc',
        if this.ring == 1 :
            print 'ring',
        if this.waist ==1:
            print 'waist',
        print this.avoid/this.total
        return this.avoid/this.total


    def getavoid(this):
        return this.avoid/this.total


    def getehp(this):
        return 1/(1-this.avoid/this.total)


    def clean(this):
        this.st = 0
        this.avoid = 0
        this.total = 0


    def tick(this,offset):
        for i in this.clock :
            i += offset

        if this.puryclock > this.puryiv :
            this.puryclock -= this.puryiv
            this.purystack += 1
            if this.purystack > 3 + this.light :
                this.purystack = 3 + this.light

        this.takemelee()
        ret = this.takephy()
        this.takemag()
        
        this.puryac(ret)

        this.stclock += this.clockoffset
        if this.stclock > this.stiv :
            this.stclock -= this.stiv
            this.sttaken += this.sttick
            this.st -= this.sttick
    #}tick

    def __init__(this,talent=['black','ht'],equip=['ring','waist'], \
            iron = 8, palm = 1.3, haste = 1.3, meleeiv = 1.5,dodgebase = 0.08, mastery = 0, magic = 0):
        random.seed()

        this.meleeiv = meleeiv  # 
        this.mastery = mastery
        this.dodgebase = dodgebase
        this.haste = haste

        blackcd = brm.Cd(90)
        kegcd = brm.Cd(8.0/haste)
        palmcd = brm.Cd(5.0/haste)
        brewcd = brm.Cd(21,3)

        for t in talent:
            if t == 'ht' or t == 'ht1' or t == 'ht10':
                this.t7 = 'ht'
                this.srate = 0.5
                this.irate = 0.9
            elif t == 'ht15':
                this.t7 = 'ht15'
                this.srate = 0.5
                this.irate = 0.9
            elif t == 'ed':
                this.t7 = 'ed'
                this.prate = 0.65
            elif t == 'bc':
                this.t7 = 'bc'
            elif t == 'black':
                this.t3 = 'black'
            elif t == 'light':
                this.t3 = 'light'
                this.light = 1
                brewcd = Cd(18,4)

        for e in equip:
            if e == '2t' :
                this.prate += 0.05
                this.srate += 0.05
            if e == '4t' :
                this.prate += 0.05
                this.srate += 0.05
                palm += 1
            if e == 'ring':
                this.ring =1
                this.stdmgrate = 1.0/26
            if e == 'waist':
                this.waist =1
                this.phrate = this.prate * 0.25
            if e == 'wrist':
                this.wrist =1
#   } init


#} class brm

if __name__ == '__main__' :
    main()
