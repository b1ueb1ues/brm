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
        'cast'
            ]

    
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

    def takemelee(this,dmg=2000000):
        this.totaltank.takemelee += dmg

        dodge = this.dodgebase + this.mastery* this.masterystack
        if this.mastery != 0:
            r = random.random()
            if r < dodge:
                this.masterystack = 0
                if this.wrist == 1 :
                    this.stackbrew.reduce(1)
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

    #########
    # isb
    def castisb(this):
        #print '--cast isb at',this.el.time,this.brewstack.stack()
        ret =this.stackbrew.cast()
        if ret != 0:
            this.isb.cast()
            this.cast.isb += 1
        else:
            print '-nobrew at',this.el.time, this.stackbrew.stack()

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
                

    ############
    # kegsmash
    class Staveoffev(Event):
        def process(this):
            this.src.castks(1)

    class Kegcd(cd):
        def endprocess(this,time):
            #print 'castks'
            this.src.castks()

    def castks(this,staveoff=0):
        if staveoff == 0:
            this.cast.ks += 1
            this.ks.cast()
        if debug >= 3:
            tmp = this.stackbrew.time()
        r = random.random()
        if r < 0.2 :
            soev = brm.Staveoffev()
            soev.time = this.el.time + 0.3
            soev.addto(this.el)

        this.stackbrew.reduce(this.kscdr)
        this.bob.reduce(this.kscdr)
        if debug >= 3:
            print 'keg at',this.el.time,
            print 'brew',tmp,'->',
            print this.stackbrew.time()
    # }kegs######

    #############
    # tigerpalm
    class Palmcd(cd):
        def endprocess(this,time):
            this.src.casttp()

    def casttp(this):
        this.tp.cast()
        this.cast.tp += 1
        if debug >= 3:
            tmp = this.stackbrew.time()
        r = random.random()
        if r < this.facepalm :
            this.stackbrew.reduce(this.tpcdr+1)
            this.bob.reduce(this.tpcdr+1)
        else:
            this.stackbrew.reduce(this.tpcdr)
            this.bob.reduce(this.tpcdr)
        if debug >= 3:
            print 'palm at',this.el.time,
            print 'brew',tmp,'->',
            print this.stackbrew.time()
    # }tpalm



    class changehaste(RepeatEvent):
        repeat = 5
        def process(this):
            if this.src.haste == 1.5 :
                this.src.haste = 1.3
            else :
                this.src.haste = 1.5


    class Bobcd(cd):
        cooldown = 90
        def endprocess(this,time):
            this.src.cast.bob += 1
            print '----castbob at',time
            brm = this.src
            stack,stackmax = brm.stackbrew.stack()
            for i in range(stack):
                brm.castisb()
            brm.stackbrew.setstack(brm.brewstackmax-1,brm.brewstackmax)
            brm.stackbrew.reduce(21)

            
            this.cast()
            print '--next bob at',this.time()


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

            if debug >= 3:
                print '--brew stack+ [%d,%d] at'%(stack,stackmax),this.now()

            if stackmax - stack <= 1:
                print 'cast pb at',this.el.time
                this.src.cast.pb += 1
                this.src.pury()
                this.cast()
        def endprocess(this,time):
            print 'cast isb(brewmax) at',this.now()
            this.src.castisb()




    def init(this):
        super(brm,this).init()
        this.init = 0

        this.staggerev = brm.StaggerEv(this.el)

        #this.ch = brm.changehaste(this.el)

        this.isbduration = 9
        this.isb = brm.ISBbuff(this,duration=this.isbduration)

        #this.ironev = brm.IronEv(this.el)

        this.gm()


        this.ks = brm.Kegcd(this,8,1)
        this.tp = brm.Palmcd(this,5,1)
        this.bob = brm.Bobcd(this)
        this.stackbrew = brm.Brewstack(this,21,1)
        this.stackbrew.setstack(this.brewstack,this.brewstackmax)

        this.castisb()
        this.ks.cast()
        this.tp.cast()
        this.bob.cast()
        print this.stackbrew.last(),this.stackbrew._cdev.time


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
    a = brm(stat=[25,50,0,20],talent=['ht'],equip=['4t'])
    a.run(200)
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
