#!/usr/bin/python2.7
# -*- encoding:utf8 -*-

from brmbase import *
from cd import *
from aura import *

#brm(talent=['black','light','ht','bc','ed'],equip=['ring','waist','wrist'], \
#            iron = 8, palmcdr = 1.3, haste = 1.3, dodgebase = 0.08, mastery = 0, crit = 0, vers = 0 ):

debug = 2

class brm(brmbase):

    statisticlist = [
        'totaltank',
        'dtb4st',
        'facetaken',
        'stin',
        'stout',
        'dodge',
            ]

    class ISBbuff(aura):
        def startprocess(this,time):
            this.src.ironskin = 1
        def endprocess(this,time):
            this.src.ironskin = 0
            this.src.castisb()
                
        def refreshprocess(this,time):
            time = this.time() + this.duration
            time2 = this.now() + this.duration * 3
            fix = time - time2
            if fix > 0 :
                this.delay(this.duration - fix)
            else:
                this.delay(this.duration)

        pass
    
    class StaggerEv(RepeatEvent):
        repeat = 0.5
        def process(this):
            this.src.takestdmg()
            #print this.src.st

    class TakePhyEv(RepeatEvent):
        repeat = 10
        dmg = 1000000
        def process(this):
            this.src.takephydmg(this.dmg)

    class TakeMagEv(RepeatEvent):
        repeat = 1
        dmg = 200000
        def process(this):
            this.src.takemagicdmg(this.dmg)

    class TakeMeleeEv(RepeatEvent):
        repeat = 1.5
        dmg = 1000000
        def process(this):
            this.src.takemelee(this.dmg)

    def gm(this):
        this.takemeleeev = brm.TakeMeleeEv(this.el,repeat = 1.5)
        this.takemeleeev.dmg = 4000000
        pass

    def krosus(this):
        this.takephyev = brm.TakePhyEv(this.el,repeat = 10)
        this.takemagev = brm.TakeMagEv(this.el,repeat = 1)
        this.takemeleeev = brm.TakeMeleeEv(this.el,repeat = 1.5)
        pass


    '''
    class PuryEv(RepeatEvent):
        repeat = 10
        def process(this):
            ret =this.src.brewstack.cast()
            print 'cast pb'
            if ret != 0:
                this.src.pury()
            else:
                print this.el.time,'nobrew',this.src.brewstack.stack()

    class IronEv(RepeatEvent):
        repeat = 9
        def process(this):
            ret =this.src.brewstack.cast()
            print 'cast isb at',this.el.time,this.src.brewstack.stack()
            if ret != 0:
                pass
            else:
                print '-nobrew at',this.el.time,this.src.brewstack.stack()
                '''

    def castisb(this):
        #print '--cast isb at',this.el.time,this.brewstack.stack()
        ret =this.brewstack.cast()
        if ret != 0:
            this.isb.cast()
        else:
            print '-nobrew at',this.el.time, this.brewstack.stack()

    ############
    # kegsmash
    class KegEv(Event):
        def process(this):
            this.src.castks(1)

    class Kegcd(cd):
        def endprocess(this,time):
            print 'castks'
            this.src.castks()

    def castks(this,staveoff=0):
        if staveoff == 0:
            this.ks.cast()
        if debug >= 2:
            tmp = this.brewstack.time()
        r = random.random()
        if r < 0.2 :
            kegev = brm.KegEv()
            kegev.time = this.el.time + 0.3
            kegev.addto(this.el)

        this.brewstack.reduce(10)
        if debug >= 1:
            print 'keg at',this.el.time,
            print 'brew',tmp,'->',
            print this.brewstack.time()
    # }kegs######

    #############
    # tigerpalm
    class PalmEv(Event):
        def process(this):
            this.src.casttp()

    class Palmcd(cd):
        def endprocess(this,time):
            print 'palm'
            this.src.casttp()

    def casttp(this):
        this.ks.cast()
        if debug >= 2:
            tmp = this.brewstack.time()
        r = random.random()
        if r < this.tpface :
            this.brewstack.reduce(tpcdr+1)
        else:
            this.brewstack.reduce(tpcdr)
        if debug >= 1:
            print 'palm at',this.el.time,
            print 'brew',tmp,'->',
            print this.brewstack.time()
    # }kegsmash

    def takemelee(this,dmg=2000000):
        this.totaltank.takemelee += dmg

        dodge = this.dodgebase + this.mastery* this.masterystack
        if this.mastery != 0:
            r = random.random()
            if r < dodge:
                this.masterystack = 0
                if this.wrist == 1 :
                    this.brewstack.reduce(1)
                    #this.blackcd.reduce(1)
                this.dodge.takemelee += dmg
                this.masterystack = 0
                return
        #else{
        dmg -= dmg * this.armorrate
        if this.ironskin == 1 :
            rate = this.irate
        else :
            rate = this.srate

        this.dtb4st.takemelee += dmg
        this.stin.takemelee += dmg * rate
        this.facetaken.takemelee += dmg * (1-rate)

        this.st += rate * dmg
        this.sttick = this.st * this.stdmgrate

        this.masterystack += 1
   #}takemelee



    class changehaste(RepeatEvent):
        repeat = 5
        def process(this):
            if this.src.haste == 1.5 :
                this.src.haste = 1.3
            else :
                this.src.haste = 1.5


    class Brewstack(stack):
        _stack = 3
        _stackmax = 3
        def stackprocess(this,time):
            if debug >= 3:
                print '------brewstack! at',time,'event at',this.time(),

            stack,stackmax = this.stack()

            if this.src.isb.enable() == 0:
                this.src.isb.cast()
                this.cast()

            if debug >= 1:
                print '--brew stack+ [%d,%d] at'%(stack,stackmax),this.now()

            if stackmax - stack <= 1:
                print 'cast pb at',this.el.time
                this.src.pury()
                this.cast()
        def endprocess(this,time):
            print 'cast isb(brewmax) at',this.now()
            this.src.castisb()




    def init(this):
        super(brm,this).init()
        this.init = 0

        this.staggerev = brm.StaggerEv(this.el)
        this.isbduration = 9
        this.isb = brm.ISBbuff(this,duration=this.isbduration)

        #this.ironev = brm.IronEv(this.el)

        this.gm()


        this.ks = brm.Kegcd(this,8,1)
        this.tp = brm.Kegcd(this,5,1)
        this.brewstack = brm.Brewstack(this,21,1)

        this.castisb()
        this.ks.cast()
        print this.brewstack.last(),this.brewstack._cdev.time


        this.init = 1

    def __init__(this,**argv):
        super(brm,this).__init__(**argv)


    def getavoid(this):
        if this.noiron != 0:
            return "%.4f|%d"%(brmbase.getavoid(this),this.noiron)
        return "%.5f\t"%(brmbase.getavoid(this))


    def showavoid(this):
        this.totaltank.showunit()
        print this.totaltank.getv()



def main():
    a = brm(haste=50)
    a.run(100)
    a.showavoid()


    return


    a = brm(equip=['4t'],talent=['black','ht10'], mastery = 30, meleetakeiv = 1.5)
    a.run(100000)
    atake = 1-a.showavoid()
    print 'brew %d + 3*%d'%(a.brewgain, a.blackgain)

    print '------'

    b = brm(equip=['4t','wrist','waist'],talent=['black','ht10'], mastery = 30, meleetakeiv = 1.5)
    b.run(100000)
    btake = 1-b.showavoid()
    print 'brew %d + 3*%d'%(b.brewgain, b.blackgain)


    print '------'
    avoid = 1-btake/atake
    print 'wrist+waist = ',avoid




#} main


if __name__ == "__main__" :
    main()
