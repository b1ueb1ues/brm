#!/usr/bin/python2.7
# -*- encoding:utf8 -*-

from brmbase import *

#brm(talent=['black','light','ht','bc','ed'],equip=['ring','waist','wrist'], \
#            iron = 8, palmcdr = 1.3, haste = 1.3, dodgebase = 0.08, mastery = 0, crit = 0, vers = 0 ):

debug = 0

class brm(brmbase):
    
    loadevent = []

    brewstackmax = 3
    brewstack = 3
    brewcd = 21

    palmcdr = 1.3
    kegcdr = 4


    class StaggerEv(RepeatEvent):
        repeat = 0.5
        def repeatproc(this):
            this.src.takestdmg()
            #print this.src.st


    class BrewcdEv(RepeatEvent):
        def repeatproc(this):
            this.src.brewstack += 1
            if this.src.brewstack >= this.src.brewstackmax :
                this.src.brewstack = this.src.brewstackmax


    class KegEv(RepeatEvent):
        def repeatproc(this):
            if this.src.brewstack < this.src.brewstackmax :
                this.src.brewcdev.move(offset = 0 - this.src.kegcdr)

    class PalmEv(RepeatEvent):
        def repeatproc(this):
            if this.src.brewstack < this.src.brewstackmax :
                this.src.brewcdev.move(offset = 0 - this.src.palmcdr)

    class IronEv(RepeatEvent):
        def repeatproc(this):
            if this.src.brewstack == this.src.brewstackmax :
                this.src.brewcdev.move(newtiming = this.time + this.src.brewcd)
            this.src.brewstack -= 1

    class BlackEv(RepeatEvent):
        def repeatproc(this):
            n = this.src.brewstack + 1
            this.src.ironev.move(offset = n * this.src.iduration)
            this.src.brewcdev.move(newtiming = this.time + this.src.brewcd)
            this.src.brewstack = this.src.brewstackmax - 1

    class ConsiderPuryEv(RepeatEvent):
        repeat = 1
        def repeatproc(this):
            if this.src.brewstack == this.src.brewstackmax :
                this.src.brewcdev.move(newtiming = this.time + this.src.brewcd)
            if this.src.brewstack >= 3 :
                this.src.pury()
                this.src.brewstack -= 1
            elif this.src.brewstack == 2 :
                if this.src.brewcdev.time - this.time < this.src.brewcd/2 :
                    this.src.pury()
                    this.src.brewstack -= 1


    class TakePhyEv(RepeatEvent):
        repeat = 1
        def repeatproc(this):
            this.src.takephydmg()




    def __init__(this):
        brmbase.__init__(this)

        if 'light' in this.talent :
            this.brewstackmax = 4
            this.brewstack = 4
            this.brewcd = 18

        this.staggerev = brm.StaggerEv(this)
        this.el.add(this.staggerev)

        this.kegev = brm.KegEv(this, repeat = 8.0 / this.haste)
        this.el.add(this.kegev)

        this.palmev = brm.PalmEv(this, repeat = 5.0 / this.haste)
        this.el.add(this.palmev)

        this.ironev = brm.IronEv(this, repeat = this.iduration)
        this.el.add(this.ironev)

        this.blackev = brm.BlackEv(this, repeat = 90.0 / this.haste)
        this.el.add(this.blackev)

        this.brewcdev = brm.BrewcdEv(this, repeat = this.brewcd)
        this.el.add(this.brewcdev)
        
        this.considerpuryev = brm.ConsiderPuryEv(this)
        this.el.add(this.considerpuryev)

        this.takephyev = brm.TakePhyEv(this)
        this.el.add(this.takephyev)

        print this.el

    def run(this, time):
        this.el.run(time)




def main():
    b = brm()
    b.run(100000)
    b.showavoid()

#} main


if __name__ == "__main__" :
    main()
