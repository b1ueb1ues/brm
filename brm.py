#!/usr/bin/python2.7
# -*- encoding:utf8 -*-

from brmbase import *

#brm(talent=['black','light','ht','bc','ed'],equip=['ring','waist','wrist'], \
#            iron = 8, palmcdr = 1.3, haste = 1.3, dodgebase = 0.08, mastery = 0, crit = 0, vers = 0 ):

class brm(brmbase):
    
    loadevent = []

    brewstackmax = 3
    brewstack = 3
    brewcd = 21

    palmcdr = 1.3
    kegcdr = 4

    def __init__(this):
        brmbase.__init__(this)

        if this.t3 == 'light' :
            this.brewstackmax = 4
            this.brewstack = 4
            this.brewcd = 18


        this.staggerev = brm.StaggerEv(this)
        this.el.add(this.staggerev)



    class StaggerEv(RepeatEvent):
        repeat = 0.5
        def repeatproc(this):
            this.src.takestdmg()
            print this.src.st

    class BrewcdEv(RepeatEvent):


    class KegEv(RepeatEvent):
        def repeatproc(this):
            this.


    def run(this, time):
        this.el.run(time)




def main():
    b = brm()
    b.st = 1000
    b.sttick = 50
    b.run(10)

#} main


if __name__ == "__main__" :
    main()
