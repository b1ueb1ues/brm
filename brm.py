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
    dodgecount = 0
    meleetakeiv = 1.5

    noiron = 0
    ed20 = 0
    ed13 = 0
    edev = 0
    fishev = 0
    edrate = 0
    fishnow = 0

    ironskin = 0

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
            this.src.fish()
            if this.src.brewstack == this.src.brewstackmax :
                this.src.brewcdev.move(newtiming = this.time + this.src.brewcd)
            if this.src.brewstack == 0:
                #print 'no iron'
                this.repeat = this.src.brewcdev.time - this.time
                blacktime = this.src.blackev.time - this.time
                if blacktime < this.repeat :
                    this.src.noiron += blacktime
                else:
                    this.src.noiron += this.repeat
                this.src.ironskin = 0
            
            if this.src.ironskin == 0 :
                this.repeat = this.src.iduration
                this.src.ironskin = 1
            this.src.brewstack -= 1
            this.src.irontimes += 1

    class BlackEv(RepeatEvent):
        def repeatproc(this):
            this.ironskin=1
            this.src.fish()
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
                this.src.fish()
                
                this.src.purytimes +=1
                this.src.brewstack -= 1
            elif this.src.brewstack == 2 :
                #if this.src.brewcdev.time - this.time < this.src.iduration :
                if this.src.brewcdev.time - this.time <= 1 : 
                    this.src.pury()
                    this.src.fish()
                    if this.src.ed13 == 1:
                        this.src.edm()
                    elif this.src.ed20 == 1:
                        this.src.edh()
                    this.src.purytimes +=1
                    this.src.brewstack -= 1

    class FishEv(Event):
        def process(this):
            this.src.dodgebase -= 0.1
            this.src.fishev = 0

    class EdmediumEv(Event):
        def process(this):
            this.src.dodgebase -= 0.133
            this.src.edev = 0
            this.src.edrate = 0

    class EdhighEv(Event):
        def process(this):
            this.src.dodgebase -= 0.20
            this.src.edev = 0
            this.src.edrate = 0

    class TakePhyEv(RepeatEvent):
        repeat = 1
        def repeatproc(this):
            this.src.takephydmg()

    class TakeMeleeEv(RepeatEvent):
        def repeatproc(this):
            this.src.takemelee()

    def edm(this):
        if this.edev != 0 :
            this.edev.rm()
            this.dodgebase -= this.edrate

        ed = brm.EdmediumEv(this)
        this.edev = ed
        ed.time = this.el.time + 6
        this.el.add(ed)
        this.dodgebase += 0.133
        this.edrate = 0.133

    def edh(this):
        if this.edev != 0 :
            this.edev.rm()
            this.dodgebase -= this.edrate

        ed = brm.EdhighEv(this)
        this.edev = ed
        ed.time = this.el.time + 6
        this.el.add(ed)
        this.dodgebase += 0.2
        this.edrate = 0.2

    def fish(this):
        if this.fishev != 0 :
            fishev.move(newtiming = this.el.time + 3)
        else :
            fish = brm.FishEv(this)
            fish.time = this.el.time + 3
            this.el.add(fish)
            this.dodgebase += 0.1

    def __init__(this,talent=['black','ht'],equip=['ring','waist'], \
            iron = 8, palmcdr = 1.3, haste = 1.3, dodgebase = 0.08, mastery = 0, crit = 0, vers = 0, meleetakeiv = 1.5 ):

        brmbase.__init__(this, talent, equip, iron, palmcdr, haste, dodgebase, mastery, crit, vers)

        this.meleetakeiv = meleetakeiv

        if 'wrist' in equip :
            this.wrist = 1

        if 'ed' in talent :
            this.ed13 = 1

        if 'ed13' in talent :
            this.ed13 = 1

        if 'ed20' in talent :
            this.ed20 = 1
        

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

        this.takemeleeev = brm.TakeMeleeEv(this, repeat = meleetakeiv)
        this.el.add(this.takemeleeev)

        #print this.el

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
                    this.brewcdev.move(-1)
                    this.blackev.move(-1)
                this.dodgecount += 1
                this.masterystack = 0
            else:
                this.takephydmg(dmg)
                this.masterystack += 1
   #}takemelee

    def run(this, time):
        this.el.run(time)

    def getavoid(this):
        if this.noiron != 0:
            return "%.4f|%d"%(brmbase.getavoid(this),this.noiron)
        return "%.5f\t"%(brmbase.getavoid(this))

    def getmavoid(this):
        avoid = (this.stout + this.puryheal + this.dodgecount*100 ) / this.totaltank
        if this.noiron != 0:
            return "%.4f|%d"%(avoid,this.noiron)
        return "%.5f\t"%(avoid)



def main():
    

    a = brm(equip=[''], mastery = 0.3, meleetakeiv = 0.5)
    a.run(100000)
    atake = 1-a.showavoid()
    print 'brew %d + 3*%d'%(a.brewgot, a.blackgot)

    print '------'

    b = brm(equip=['wrist','waist'], mastery = 0.3, meleetakeiv = 0.5)
    b.run(100000)
    btake = 1-b.showavoid()
    print 'brew %d + 3*%d'%(b.brewgot, b.blackgot)


    print '------'
    avoid = 1-btake/atake
    print 'wrist+waist = ',avoid




#} main


if __name__ == "__main__" :
    main()
