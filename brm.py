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
    brewcd = 21.0
    brewgot = 0
    blackgot = 1

    palmcdr = 1.3
    kegcdr = 4

    purytimes = 0
    irontimes = 0
    kegtimes = 0
    palmtimes = 0

    wrist = 0
    misscount = 0

    class StaggerEv(RepeatEvent):
        repeat = 0.5
        def repeatproc(this):
            this.src.takestdmg()
            #print this.src.st


    class BrewcdEv(RepeatEvent):
        def repeatproc(this):
            this.src.brewgot += 1
            this.src.brewstack += 1
            if this.src.brewstack >= this.src.brewstackmax :
                this.src.brewstack = this.src.brewstackmax


    class KegEv(RepeatEvent):
        def repeatproc(this):
            this.src.kegtimes += 1
            if this.src.brewstack < this.src.brewstackmax :
                this.src.brewcdev.move(offset = 0 - this.src.kegcdr)

                timing = this.src.blackev.time - this.src.kegcdr
                if timing < this.el.time :
                    this.src.blackev.move(newtiming = this.el.time)
                else:
                    this.src.blackev.move(newtiming = timing)


    class PalmEv(RepeatEvent):
        def repeatproc(this):
            this.src.palmtimes += 1
            if this.src.brewstack < this.src.brewstackmax :
                this.src.brewcdev.move(offset = 0 - this.src.palmcdr)

                timing = this.src.blackev.time - this.src.palmcdr
                if timing < this.el.time :
                    this.src.blackev.move(newtiming = this.el.time)
                else:
                    this.src.blackev.move(newtiming = timing)

    class IronEv(RepeatEvent):
        def repeatproc(this):
            if this.src.brewstack == this.src.brewstackmax :
                this.src.brewcdev.move(newtiming = this.time + this.src.brewcd)
            if this.src.brewstack == 0:
                print 'no iron'
            this.src.brewstack -= 1
            this.src.irontimes += 1

    class BlackEv(RepeatEvent):
        def repeatproc(this):
            this.src.blackgot += 1
            n = this.src.brewstack + 1
            this.src.ironev.move(offset = n * this.src.iduration)
            this.src.brewcdev.move(newtiming = this.el.time + this.src.brewcd)
            this.src.brewstack = this.src.brewstackmax - 1
            this.src.irontimes += n

    class ConsiderPuryEv(RepeatEvent):
        repeat = 1
        def repeatproc(this):
            if this.src.brewstack == this.src.brewstackmax :
                this.src.brewcdev.move(newtiming = this.time + this.src.brewcd)
            if this.src.brewstack >= 3 :
                this.src.pury()
                this.src.purytimes +=1
                this.src.brewstack -= 1
            elif this.src.brewstack == 2 :
                if this.src.brewcdev.time - this.time < this.src.iduration :
                    this.src.pury()
                    this.src.purytimes +=1
                    this.src.brewstack -= 1


    class TakePhyEv(RepeatEvent):
        repeat = 1
        def repeatproc(this):
            this.src.takephydmg()

    class TakeMeleeEv(RepeatEvent):
        repeat = 1.5
        def repeatproc(this):
            this.src.takemelee()


    def __init__(this,talent=['black','ht'],equip=['ring','waist'], \
            iron = 8, palmcdr = 1.3, haste = 1.3, dodgebase = 0.08, mastery = 0, crit = 0, vers = 0 ):
        brmbase.__init__(this, talent, equip, iron, palmcdr, haste, dodgebase, mastery, crit, vers)


        if 'wrist' in this.equip :
            this.wrist = 1


        this.staggerev = brm.StaggerEv(this)
        this.el.add(this.staggerev)

        this.kegev = brm.KegEv(this, repeat = 8.0 / this.haste)
        this.el.add(this.kegev)

        this.palmev = brm.PalmEv(this, repeat = 5.0 / this.haste)
        this.el.add(this.palmev)

        this.ironev = brm.IronEv(this, repeat = this.iduration)
        this.el.add(this.ironev)

        this.blackev = brm.BlackEv(this, repeat = 90.0)
        this.el.add(this.blackev)

        this.brewcdev = brm.BrewcdEv(this, repeat = this.brewcd)
        this.el.add(this.brewcdev)
        
        this.considerpuryev = brm.ConsiderPuryEv(this)
        this.el.add(this.considerpuryev)

       # this.takephyev = brm.TakePhyEv(this)
       # this.el.add(this.takephyev)

        this.takemeleeev = brm.TakeMeleeEv(this)
        this.el.add(this.takemeleeev)

        print this.el

    def takemelee(this,dmg=100,rate=0.9):
        this.totaltank += dmg
        this.meleecount += 1
        if this.mastery == 0:
            this.takephydmg(dmg)
        else :
            r = random.random()
            dodge = this.dodgebase + this.mastery* this.masterystack
            if r < dodge:
                #doged!
                if this.wrist == 1 :
                    #print '%.2f: '%this.el.time,
                    #print this.brewcdev,
                    this.brewcdev.move(-1)
                    this.blackev.move(-1)
                    this.misscount += 1
                this.masterystack = 0
            else:
                this.takephydmg(dmg)
                this.masterystack += 1
   #}takemelee

    def run(this, time):
        this.el.run(time)




def main():

    #b = brm(equip=[''])
    #b.run(100000)
    #b.showavoid()

   # a = brm(equip=['wrist'], mastery = 0.3, palmcdr= 1)
   # a.run(100)
   # atake = 1-a.showavoid()
   # print a.wristtimes

   # a = brm(equip=['wrist'],mastery= 0.3)
   # a.run(100000)
   # a.showavoid()
   # print 'a wrist', a.wristtimes
   # print 'a purytimes',a.purytimes
   # print 'a irontimes',a.irontimes
   # print 'a palm',a.palmtimes
   # print 'a keg',a.kegtimes
   # print 'a brewgot',a.brewgot
   # print 'a blackgot',a.blackgot

   # exit()

    a = brm(equip=['wrist'], mastery = 0.3)
    a.run(100000)
    atake = 1-a.showavoid()

    print '------'

    b = brm(equip=['wrist'], mastery = 0.4)
    b.run(100000)
    btake = 1-b.showavoid()

    print '------'
    c = brm(equip=['wrist'], mastery = 0.3, haste = 1.4)
    c.run(100000)
    ctake = 1-c.showavoid()

    avoid = 1-btake/atake
    print avoid

    avoid = 1-ctake/atake
    print avoid

    print 'a misscount', a.misscount

    print 'a purytimes',a.purytimes
    print 'b purytimes',b.purytimes
    print 'a brewgot',a.brewgot
    print 'b brewgot',b.brewgot


#} main


if __name__ == "__main__" :
    main()
