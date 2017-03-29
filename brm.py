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
    blackstack = 1
    blackstackmax = 1
    blackenablestart = 0
    blackcd = 90.0
    brewcd = 21.0
    brewgain = 0
    blackcd = 90.0
    blackgain = 0

    selfhrate = 0.05
    t20hrate = 0.8
    t20heal = 0.0


    palmcdr = 1.4
    kegcdr = 4

    purycount = 0
    ironcount = 0
    kegcount = 0
    palmcount = 0
    brewcdwaste = 0
    blackcdwaste = 0
    fishtime = 0
    edtime = 0
    timeran = 0

    wrist = 0
    dodgecount = 0
    meleetakeiv = 1.5

    noiron = 0
    ed20 = 0
    ed13 = 0
    edev = 0
    fishev = 0
    edrate = 0

    fishstart = 0
    edenable = 0

    ironskin = 1
    
    magic = 0
    
    newfuzan = 0

    quicksip = 0
    qspurified = 0
    staveoff = 0
    
    t20pury = 0

    class t20Ev(RepeatEvent):
        def repeatproc(this):
            #this.src.t20heal += 100 * this.src.t20hrate
            this.src.stout += 0.25 * this.src.st
            this.src.t20pury += 0.25 * this.src.st
            this.src.st -= 0.25 * this.src.st
            this.src.sttick -= this.src.sttick * 0.25
            #print this.src.st

    



    class StaggerEv(RepeatEvent):
        repeat = 0.5
        def repeatproc(this):
            this.src.takestdmg()
            #print this.src.st


    class BrewcdEv(RepeatEvent):
        def repeatproc(this):
            this.src.brewgain += 1
            this.src.brewstack += 1
            if this.src.brewstack >= this.src.brewstackmax :
                this.src.brewstack = this.src.brewstackmax


    kegintl = 0
    class KegEv(RepeatEvent):
        realrepeat = 0
        def repeatproc(this):
            if this.repeat != this.realrepeat :
                this.repeat = this.realrepeat 

            blackremain = this.src.blackev.time - this.time 

            if this.src.kegintl == 1 and this.repeat != 0:
                if blackremain < 1:
                    this.repeat = this.src.blackev.time - this.time + 0.01
                    return

            if this.src.blackstack == 1:
                this.src.blackcdwaste += this.src.kegcdr
            elif blackremain < this.src.kegcdr :
                this.src.blackcdwaste += this.src.kegcdr - blackremain

            this.src.kegcount += 1
            if this.src.brewstack < this.src.brewstackmax :
                this.src.brewcdev.move(offset = 0 - this.src.kegcdr)

                timing = this.src.blackev.time - this.src.kegcdr

                if timing < this.el.time :
                    this.src.blackev.move(newtiming = this.el.time)
                else:
                    this.src.blackev.move(newtiming = timing)

            if this.src.staveoff != 0 and this.repeat != 0:
                r = random.random()
                if r <= 0.2 :
                    this.src.sokegev = brm.KegEv(this.src,time=this.time+0.01,repeat = 0)
                    this.src.sokegev.realrepeat = 0
                    this.el.add(this.src.sokegev)


    class PalmEv(RepeatEvent):
        def repeatproc(this):
            this.src.palmcount += 1
            if this.src.brewstack < this.src.brewstackmax :
                this.src.brewcdev.move(offset = 0 - this.src.palmcdr)

                timing = this.src.blackev.time - this.src.palmcdr
                if timing < this.el.time :
                    this.src.blackev.move(newtiming = this.el.time)
                else:
                    this.src.blackev.move(newtiming = timing)

            blackremain = this.src.blackev.time - this.time 
            if this.src.blackstack == 1:
                this.src.blackcdwaste += this.src.palmcdr
            elif blackremain < this.src.palmcdr :
                this.src.blackcdwaste += this.src.palmcdr - blackremain

    class IronEv(RepeatEvent):
        def repeatproc(this):
            this.src.fish()
            if this.src.brewstack == this.src.brewstackmax :
                this.src.brewcdev.move(newtiming = this.time + this.src.brewcd)
            if this.src.brewstack == 0:
                #print 'no iron'
                this.repeat = this.src.brewcdev.time - this.time + 0.01
                blacktime = this.src.blackev.time - this.time
                if blacktime < this.repeat :
                    this.src.noiron += blacktime
                else:
                    this.src.noiron += this.repeat
                this.src.ironskin = 0
                return
            
            if this.src.ironskin == 0 :
                this.repeat = this.src.iduration
                this.src.ironskin = 1
            this.src.brewstack -= 1
            this.src.ironcount += 1

            if this.src.newfuzan != 0 :
                this.src.st -= this.src.st * 0.05
                this.src.sttick -= this.src.sttick * 0.05


    blackintl = 1
    class BlackEv(RepeatEvent):
        def repeatproc(this):
            if 'black' not in this.src.talent :
                return 

            brewcdremain = this.src.brewcdev.time - this.time
            this.src.blackstack = 0

            if this.repeat != 90 :
                this.repeat = 90
            elif this.src.blackintl == 1:
#                brewcdremain = this.src.brewcdev.time - this.time
#                this.repeat = brewcdremain + 0.1
#                return
                if brewcdremain < this.src.brewcd / 2 :
                    this.repeat = brewcdremain + 0.01
                    this.blackstack = 1
                    this.src.blackcdwaste += brewcdremain + 0.01
                    return
                   # newev = brm.BlackEv(this.src, repeat = 90, time = this.src.brewcdev.time + 0.1)
                   # this.src.blackev = newev
                   # this.el.add(this.src.blackev)
                   # this.repeat = 0
                   # return

            this.src.brewcdwaste += this.src.brewcd - brewcdremain

            this.ironskin=1
            this.src.fish()
            this.src.blackgain += 1
            n = this.src.brewstack + 1
            this.src.ironev.move(offset = n * this.src.iduration)
            this.src.brewcdev.move(newtiming = this.el.time + this.src.brewcd)
            this.src.brewstack = this.src.brewstackmax - 1
            this.src.ironcount += n
            this.src.brewgain += 3

            for i in range(n):
                this.src.qspury()

            tmpev = brm.PalmEv(this.src,repeat=0)
            tmpev.time = this.time + 0.01
            tmpev.addto(this.el)

            tmpev = brm.PalmEv(this.src,repeat=0)
            tmpev.time = this.time + 0.02
            tmpev.addto(this.el)

    class ConsiderPuryEv(RepeatEvent):
        repeat = 1
        def repeatproc(this):
            #print '%.2f|%.2f '%(this.src.masterystack*this.src.mastery,  this.src.dodgebase)
          #  print this.src.ironskin
          #  print this.src.el
            if this.src.brewstack == this.src.brewstackmax :
                this.src.brewcdev.move(newtiming = this.time + this.src.brewcd)
            if this.src.brewstack >= 3 :
                this.src.pury()
                this.src.qsiron()
                this.src.fish()

                if this.src.ed13 == 1:
                    this.src.edm()
                elif this.src.ed20 == 1:
                    this.src.edh()
                
                this.src.purycount +=1
                this.src.brewstack -= 1
            elif this.src.brewstack == 2 :
                #if this.src.brewcdev.time - this.time < this.src.iduration :
                if this.src.brewcdev.time - this.time <= 8 : 
                    this.src.pury()
                    this.src.qsiron()
                    this.src.fish()

                    if this.src.ed13 == 1:
                        this.src.edm()
                    elif this.src.ed20 == 1:
                        this.src.edh()
                    this.src.purycount +=1
                    this.src.brewstack -= 1

    class FishEv(Event):
        def process(this):
            this.src.dodgebase -= 0.1
            this.src.fishev = 0
            this.src.fishtime += this.time - this.src.fishstart #statis

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

    class TakeMagEv(RepeatEvent):
        repeat = 1
        def repeatproc(this):
            this.src.takemagicdmg()

    def qspury(this):
        #print this.st, this.qspurified
        if this.quicksip != 0 :
            this.qspurified += this.st * 0.05
            this.st -= this.st * 0.05
            this.sttick -= this.sttick * 0.05

    def qsiron(this):
        if this.quicksip != 0 :
            this.ironev.move(offset = 1)
    

    def edm(this):
        if this.edev != 0 :
            this.edev.rm()
            this.dodgebase -= this.edrate
            this.edtime -= 6 - (this.el.time - this.edev.time)

        this.edtime += 6

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
            this.edtime -= 6 - (this.el.time - this.edev.time)

        this.edtime += 6

        ed = brm.EdhighEv(this)
        this.edev = ed
        ed.time = this.el.time + 6
        this.el.add(ed)
        this.dodgebase += 0.2
        this.edrate = 0.2

    def fish(this):
        if this.fishev != 0 :
            this.fishev.move(newtiming = this.el.time + 4.5)
        else :
            fish = brm.FishEv(this)
            fish.time = this.el.time + 4.5
            this.el.add(fish)
            this.fishev = fish
            this.dodgebase += 0.1
            this.fishstart = this.el.time #statis

    def __init__(this,conf=0,talent=['black','ht'],equip=['ring','waist'], \
            iduration = 8, palmcdr = 1.3, haste = 1.3, dodgebase = 0.1, mastery = 0.27, crit = 0.25, vers = 0.1, meleetakeiv = 1.50 ,melee = 1, magic = 0, newfuzan = 0, t20rppm = 5):

        brmbase.__init__(this,conf,talent, equip, iduration, palmcdr, haste, dodgebase, mastery, crit, vers)

        this.meleetakeiv = meleetakeiv
        this.magic = magic
        this.melee = melee

        this.quicksip = newfuzan
        this.staveoff = newfuzan
        this.newfuzan = newfuzan
    
        this.newfuzan = newfuzan


        #print this.crit,this.haste,this.vers,this.mastery
        #print this.stat
        if 'wrist' in this.equip :
            this.wrist = 1

        if 't20' in this.equip:
            this.t20rppm = t20rppm
            this.t20ev = brm.t20Ev(this, repeat = 60.0/t20rppm)
            this.el.add(this.t20ev)

        if 'ed' in this.talent :
            this.ed13 = 1

        if 'ed13' in this.talent :
            this.ed13 = 1

        if 'ed20' in this.talent :
            this.ed20 = 1
        

        this.staggerev = brm.StaggerEv(this)
        this.el.add(this.staggerev)

        this.kegev = brm.KegEv(this, repeat = 8.0 / this.haste)
        this.kegev.realrepeat = 8.0/this.haste
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

        if this.melee != 0:
            this.takemeleeev = brm.TakeMeleeEv(this, repeat = meleetakeiv)
            this.el.add(this.takemeleeev)

        if this.magic != 0 :
            this.takemagev = brm.TakeMagEv(this)
            this.el.add(this.takemagev)



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

    def takemagicdmg(this):
        dmg = 100
        if this.ironskin == 1 :
            rate = this.irate * 0.7
        else :
            rate = this.srate * 0.7
        this.totaltank += dmg
        this.dtb4st += dmg
        this.stin += rate * dmg
        this.st += rate * dmg
        this.sttick = this.st * this.stdmgrate



    def run(this, time):
        this.timeran = time
        this.el.run(time)

    def getavoid(this):
        if this.noiron != 0:
            return "%.4f|%d"%(brmbase.getavoid(this),this.noiron)
        return "%.5f\t"%(brmbase.getavoid(this))

    def getehr(this):
        vers = this.vers
        crit = this.crit
        mastery = this.mastery
        selfh = this.dtb4st*this.selfhrate*(1.0-vers/2) \
            *(1.0+crit)*(1.0+crit*0.65)*(1.0+vers)*(1.0+mastery)
        realdt = (this.facetaken + this.sttaken) * (1.0-vers/2)
        ehrb4 = realdt - selfh - this.puryheal - this.t20heal
        ehr = ehrb4 / (1.0+0.65*crit) 
        ehrpdt = ehr / this.totaltank
        #print selfh, realdt
        return ehrpdt

    def getehrr(this):
        return 1-this.getehr()


    def getmavoid(this):
        avoid = (this.stout + this.puryheal + this.dodgecount*100 ) / this.totaltank
        if this.noiron != 0:
            return "%.4f|%d"%(avoid,this.noiron)
        return "%.5f\t"%(avoid)

    def showavoid(this):
        ret = brmbase.showavoid(this)
        print 'simc time',this.timeran
        print 'brewgain',this.brewgain
        print 'ironskin *',this.ironcount
        print 'purify *',this.purycount
        print 'blackox *',this.blackgain
        print 'brew-stache %d%%'%int(this.fishtime/this.timeran*100)
        if this.edtime != 0 :
            print 'elusive dance %d%%'%int(this.edtime/this.timeran*100)
        print 'blackcdwaste %d (%d stackbrew)'%(this.blackcdwaste, 3*this.blackcdwaste/90)
        print 'brewcdwaste from BOB %d (%d stackbrew)'%(this.brewcdwaste, this.brewcdwaste/this.brewcd)
        print 'totalwaste %d stackbrew'%(3*this.blackcdwaste/90+this.brewcdwaste/this.brewcd)

        if this.t20heal != 0:
            print 't20heal %d'%this.t20heal
        if this.t20pury != 0 :
            print '4t20pury %d(%.2f%%)'%(this.t20pury, this.t20pury/this.stin*100)

        if this.newfuzan != 0 :
            print 'qspurified %d(%.2f%%)'%(this.qspurified,this.qspurified/this.stin*100)
        #print 'kegcount %d'%this.kegcount
        return ret



def main():

    a = brm(equip=[''], mastery = 0.3, meleetakeiv = 0.5)
    a.run(100000)
    atake = 1-a.showavoid()
    print 'brew %d + 3*%d'%(a.brewgain, a.blackgain)

    print '------'

    b = brm(equip=['wrist','waist'], mastery = 0.3, meleetakeiv = 0.5)
    b.run(100000)
    btake = 1-b.showavoid()
    print 'brew %d + 3*%d'%(b.brewgain, b.blackgain)


    print '------'
    avoid = 1-btake/atake
    print 'wrist+waist = ',avoid




#} main


if __name__ == "__main__" :
    main()
