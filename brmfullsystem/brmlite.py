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
        repeat = 1
        def process(this):
            this.src.takephydmg()

    class TakeMagEv(RepeatEvent):
        repeat = 1
        def process(this):
            this.src.takemagicdmg()

    class PuryEv(RepeatEvent):
        repeat = 6
        def process(this):
            this.src.pury()

    class changehaste(Event):
        def process(this):
            this.src.haste = 1


    def init(this):
        super(brm,this).init()

        this.init = 0

        this.staggerev = brm.StaggerEv(this.el)
        this.puryev = brm.PuryEv(this.el)
        this.takephyev = brm.TakePhyEv(this.el)
        this.takemagev = brm.TakeMagEv(this.el)
        this.changehaste = brm.changehaste(this.el,time=5)

        this.kegcd = cd(this,12,1)
        this.somecd = cd(this,3)
        
        this.kegcd.cast()
        this.somecd.cast()


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
    a = brm(haste=100)
    a.run(13)
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
