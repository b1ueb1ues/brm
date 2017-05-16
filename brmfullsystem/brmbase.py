#!/usr/bin/python2.7
# -*- encoding:utf8 -*-

import random
import copy
from event import *
from statistic import *
debug = 0

def main():
#    b = brmbase(talent=['black','light','ht','bc','ed'],equip=['ring','waist','wrist'], stat=[25,25,0,20],\
#            iduration = 8, palmcdr = 1.4, haste = 30, dodgebase = 0.08, mastery = 0, crit = 0, vers = 0 )

    b = brmbase(stat=[30,20,0,16],equip=['ring','waist','4t'],iduration=9)
    b.haste=32
    b.init()
    print b.__dict__

    class test(brmbase):
        def run(this):
            print 'hello'
            this.ev = RepeatEvent(this.el,repeat=1)
            print this.el
            super(test,this).run(100)

    t = test(stat=[25,25,0,20])
    t.run()


class brmbase(object):

    #ed : elusive dance
    #ht : high tolerance
    #bc : blackout combo


    fout = 0
    el = 0
    conf = 0
    initialized = 0
    initargv = {}
    
    hp = 6000000
    hpmax = 6000000
    energy = 100
    ap = 0
    armor = 4400
    armorrate = 0

    talent = []
    equip = []
    stat = []

    ring = 0
    waist = 0
    wrist = 0
    chest = 0

    #stat
    dodgebase = 0.10
    crit = 0.1
    haste = 1.3
    vers = 0
    mastery = 0.3
    masterystack = 0


    isbduration = 8
    kscdr = 4
    tpcdr = 1.4
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
    class meleecount(statistic):
        pass
    class dodgecount(statistic):
        pass
    class dodgecount(statistic):
        pass
    class dtb4st(statistic):
        pass
    class totaltank(statistic):
        pass
    class stin(statistic):
        pass
    class stout(statistic):
        pass
    class facetaken(statistic):
        pass

    #totaltank = 0
    #sttaken = 0
    #stin = 0
    #pbpury = 0
    waistheal = 0



    takephydmg_totaltank = totaltank(src='takephydmg')
    takephydmg_dtb4st = dtb4st(src='takephydmg')
    takephydmg_stin = stin(src='takephydmg')
    takephydmg_facetaken = facetaken(src='takephydmg')

    def takephydmg(this,dmg=4000000,rate=0.9):
        this.takephydmg_totaltank += this.dmg
        dmg -= dmg * this.armorrate
        
        if this.ironskin == 1 :
            rate = this.irate
        else :
            rate = this.srate

        this.takephydmg_dtb4st += dmg
        this.takephydmg_stin += rate * dmg
        this.takephydmg_facetaken += dmg * (1-rate)

        this.st += rate * dmg
        this.sttick = this.st * this.stdmgrate


    takemagicdmg_totaltank = totaltank(src='takemagicdmg')
    takemagicdmg_dtb4st = dtb4st(src='takemagicdmg')
    takemagicdmg_stin = stin(src='takemagicdmg')
    takemagicdmg_facetaken = facetaken(src='takemagicdmg')

    def takemagicdmg(this,dmg=400000):
        if this.ironskin == 1 :
            rate = this.irate * 0.7
        else :
            rate = this.srate * 0.7
        this.takemagicdmg_totaltank += dmg
        this.takemagicdmg_dtb4st += dmg
        this.takemagicdmg_stin += dmg * rate
        this.takemagcidmg_facetaken += dmg * (1-rate)

        this.st += rate * dmg
        this.sttick = this.st * this.stdmgrate


    takemelee_totaltank = totaltank(src='takemelee')
    takemelee_dtb4st = dtb4st(src='takemelee')
    takemelee_stin = stin(src='takemelee')
    takemelee_facetaken = facetaken(src='takemelee')

    def takemelee(this,dmg=4000000,rate=0.9):
        takemelee_totaltank += dmg
        if this.mastery == 0:
            this.takephydmg(dmg)
        else :
            r = random.random()
            dodge = this.dodgebase + this.mastery* this.masterystack
            if r < dodge:
                this.masterystack = 0
            else:
                dmg -= dmg * this.armorrate
                if this.ironskin == 1 :
                    rate = this.irate
                else :
                    rate = this.srate

                this.takemelee_dtb4st += dmg
                this.takemelee_stin += dmg * rate
                this.takemelee_facetaken += dmg * (1-rate)

                this.st += rate * dmg
                this.sttick = this.st * this.stdmgrate

                this.masterystack += 1
   #}takemelee

    st_stout = stout(src='takestdmg')
    def takestdmg(this):
        if this.st <= 0 :
            return
        this.st_stout += this.sttick
        this.st -= this.sttick

    def pury(this,rate=-1,src='pb'):
        if rate == -1 :
            prate = this.prate
        else :
            prate = rate

        pr_stout = brm.stout(src=src)
        pr_stout += this.st * prate

        #print this.el.time,this.st,this.st * this.prate
        if rate == -1 and this.phrate != 0 :
            this.puryheal += this.phrate * this.st * ( 1 + this.crit * 0.65 )
        this.st -= this.st * prate
        this.sttick -= this.sttick * prate

    def showavoid(this):
        print 'stat\t',this.stat
        print 'talent\t',this.talent
        print 'equip\t',this.equip
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


    '''
    def __setattr__(this,name,value):
        if this.init != 0:
            if name == 'conf' :
                tmpconf = conf
            else :
                tmpconf = this.conf
            tmpconf.__setattr__(name,value)
            this.refresh(tmpconf)
            return

        super.__setattr__(this,name,value)
        '''

    def refresh(this):
        'unstable'
        initargv = this.initargv
        tmpdic = copy.deepcopy(this.__dict__)
        tmpdic.pop('conf')
        for i in tmpdic :
            this.__delattr__(i)
        this.__init__(transfer=tmpdic)
        return

    def run(this, time=9999):
        #this.refresh()
        this.init()
        this.timeran = time
        this.el.run(time)

    def statsync(this):
        attr = this.__dict__
        
        if 'crit' in attr:
            this.stat[0] = attr['crit']
        if 'haste' in attr:
            this.stat[1] = attr['haste']
        if 'vers' in attr:
            this.stat[2] = attr['vers']
        if 'mastery' in attr:
            this.stat[3] = attr['mastery']

        this.crit = this.stat[0]
        this.haste = this.stat[1]
        this.vers = this.stat[2]
        this.mastery = this.stat[3]

        this.stat[2] = '%.2f/%.2f'%(this.vers,float(this.vers)/2)

        this.crit = float (this.crit) / 100
        this.haste = float (this.haste) / 100 + 1
        this.vers = float (this.vers) / 100
        this.mastery = float (this.mastery) / 100


    def gethaste(this):
        return this.haste

    def getarmorrate(this,level=113):
        level = str(level)
        armorC= {
            '110':7390,
            '111':7648,
            '112':7906,
            '113':8164
        }
        C = armorC[level]
        return this.armor / (this.armor + C)

    def setup(this):
        argv = this.initargv
        for a in argv:
            this.__setattr__(a,argv[a])


    def init(this):
        if this.initialized != 0 :
           print 'dirty brmbase'
           exit()
        this.setup()
        this.statsync()

        this.armorrate = this.getarmorrate()

        for t in this.talent:
            if t == 'ht' or t == 'ht1' or t == 'ht10':
                this.srate += 0.10
                this.irate += 0.10
                '''
                this.haste *= 1.1
            elif t == 'ht15':
                this.srate += 0.10
                this.irate += 0.10
                this.haste *= 1.15
                '''
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
            if e == '2t19' :
                this.irate += 0.05
                this.srate += 0.05
            if e == '4t19' :
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
            if e == 'chest':
                this.chest =1

        this.brewcd /= this.haste
        this.initialized = 1
        
    def __init__(this,**argv):
        this.initargv = argv

        random.seed(1)

        this.el = Eventlist()
        this.el.src = this

        this.talent = ['black']
        this.equip = ['4t']
        this.stat = [25,25,0,25]

    #}init
#}class brmbase



if __name__ == '__main__' :
    main()
