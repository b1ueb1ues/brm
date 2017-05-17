#!/usr/bin/python2.7
# -*- encoding:utf8 -*-

from brmbase import *
from cd import *

#brm(talent=['black','light','ht','bc','ed'],equip=['ring','waist','wrist'], \
#            iron = 8, palmcdr = 1.3, haste = 1.3, dodgebase = 0.08, mastery = 0, crit = 0, vers = 0 ):

debug = 0

class brm(brmbase):
    
    class StaggerEv(RepeatEvent):
        repeat = 0.5
        def process(this):
            this.src.takestdmg()
            #print this.src.st

    class TakePhyEv(RepeatEvent):
        repeat = 10
        def process(this):
            this.src.takephydmg()

    class TakeMagEv(RepeatEvent):
        repeat = 1
        def process(this):
            this.src.takemagicdmg()

    class TakeMeleeEv(RepeatEvent):
        repeat = 1.5
        def process(this):
            this.src.takemelee()


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
                '''

    class IronEv(RepeatEvent):
        repeat = 9
        def process(this):
            ret =this.src.brewstack.cast()
            print 'cast isb at',this.el.time
            if ret != 0:
                this.src.pury()
            else:
                print this.el.time,'nobrew',this.src.brewstack.stack()

    class changehaste(RepeatEvent):
        repeat = 5
        def process(this):
            if this.src.haste == 1.5 :
                this.src.haste = 1.3
            else :
                this.src.haste = 1.5

    class Kegcd(cd):
        def endprocess(this,time):
            print 'keg at',time,
            print 'brew',this.src.brewstack.time(),'->',
            this.src.brewstack.reduce(6)
            print this.src.brewstack.time(),this.src.brewstack._cdev.el._hastelist
            this.cast()

    class Brewstack(stack):
        _stack = 3
        _stackmax = 3
        def stackprocess(this,time):
            print '------brewstack! at',time,'event at',this.time(),
            stack,stackmax = this.stack()
            print '[%d,%d]'%(stack,stackmax),this._cdev.el._hastelist
            if stackmax - stack <= 1:
                print 'cast pb at',this.el.time
                this.cast()





    def init(this):
        super(brm,this).init()

        this.init = 0

        this.staggerev = brm.StaggerEv(this.el)
        this.ironev = brm.IronEv(this.el)
        this.takephyev = brm.TakePhyEv(this.el)
        this.takemagev = brm.TakeMagEv(this.el)


        this.kegcd = brm.Kegcd(this,8,1)
        this.brewstack = brm.Brewstack(this,21,1)

        this.brewstack.cast()
        this.kegcd.cast()
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
    a.run(50)
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
