#!/usr/bin/python2.7
# -*- encoding:utf8 -*-
import random
class Brmfull:
    #ed : elusive dance
    #ht : high tolerance
    #bc : blackout combo
    class Cd:
        max = 0
#   }

    class Event:
        clock = 0
        def __init__(this,clock = 0):
            this.clock = clock
        def __repr__(self):
            return "event at %d"%this.clock
        def __str__(self):
            return "event at %d"%this.clock

        def process(this):
            pass
#   }

    class Eventlist:
        e = Event()
        el = [e]
        def add(event):
            timing = event.clock()
            





    fout = 0
    clock = 0
    clockoffset = 0.1

    t3 = ''
    t7 = ''
    light = 0

    ring = 0
    waist = 0
    wrist = 0

    dodgebase = 0.08
    mastery = 0.3
    haste = 1.3

    iduration = 7.5
    palm = 1.3

    st = 0  # stagger pool
    sttick = 0 # stagger tick

    prate = 0.5 # purify rate
    phrate = 0  # purify healrate
    srate = 0.4 # stagger rate
    irate = 0.8 # stagger rate (ironskin)

    total = 0 # total dmg taken
    avoid = 0 # avoidance
    facetotal = 0
    sttaken = 0
    stin = 0

    stdmgrate = 1.0/20 # stagger dmg rate

    f = 0

    stclock = 0
    stiv = 0.5 #stagger interval
    meleeclock = 0
    meleeiv = 1.5

    masterystack = 0



    brewstack = 3
    brewmax = 3
    brewclock = 0
    brewcd = 21
    
    blackcd = 90
    blackclock = 0

    kegcd = 8
    palmcd = 5

    def __init__(this,talent=['black','ht'],equip=['ring','waist'], \
            iron = 8, palm = 1.3, haste = 1.3, meleeiv = 1.5,dodgebase = 0.08, mastery = 0):
        random.seed()

        this.meleeiv = meleeiv  # 
        this.mastery = mastery
        this.dodgebase = dodgebase
        this.haste = haste

        for t in talent:
            if t == 'ht' or t == 'ht1' or t == 'ht10':
                this.t7 = 'ht'
                this.srate = 0.5
                this.irate = 0.9
            elif t == 'ht15':
                this.t7 = 'ht15'
                this.srate = 0.5
                this.irate = 0.9
            elif t == 'ed':
                this.t7 = 'ed'
                this.prate = 0.65
            elif t == 'bc':
                this.t7 = 'bc'
            elif t == 'black':
                this.t3 = 'black'
            elif t == 'light':
                this.t3 = 'light'
                this.brewcd = 18
                this.brewmax = 4
                this.light = 1
        this.blackcd /= haste
        this.brewcd /= haste
        this.kegcd /= haste
        this.palmcd /= haste

        for e in equip:
            if e == '2t' :
                this.prate += 0.05
                this.srate += 0.05
            if e == '4t' :
                this.prate += 0.05
                this.srate += 0.05
                palm += 1
            if e == 'ring':
                this.ring =1
                this.stdmgrate = 1.0/26
            if e == 'waist':
                this.waist =1
                this.phrate = this.prate * 0.25
            if e == 'wrist':
                this.wrist =1

#   } init

    def dmgtaken(this,dmg=100,rate=0.9):
        this.total += dmg
        this.stin += rate * dmg
        this.st += rate * dmg
        this.sttick = this.st * this.stdmgrate

    def magictaken(this,dmg=100,rate=0.9):
        this.total += dmg
        this.stin += rate/2 * dmg 
        this.st += rate/2 * dmg
        this.sttick + this.st * this.stdmgrate

    def takemelee(this):
        rate = 0.9
        this.meleeclock += this.clockoffset
        if this.meleeclock > this.meleeiv :
            this.meleeclock -= this.meleeiv
            if this.mastery == 0:
                this.total += 100.0
                this.stin += rate * 100
                this.st += rate * 100
                this.sttick = this.st * this.stdmgrate
            else :
                r = random.random()
                dodge = this.dodgebase + this.mastery* this.masterystack
                if r < dodge:
                    this.masterystack = 0
                    if this.wrist == 1:
                        this.puryclock+=1
                    return
                else:
                    this.total += 100.0
                    this.st += rate * 100
                    this.sttick = this.st * this.stdmgrate
                    this.masterystack += 1
#   }

    phyclock = 0
    def takephy(this):
        this.phyclock += this.clockoffset
        if this.phyclock > 20 :
            this.phyclock -= 20
            this.dmgtaken(200)
            return 1

        return 0

    def takemag(this):
        pass

    def puryac(this,ret):
            
        if ret == 1 and this.purystack > 0:
            this.pury()
        elif ret == 0 and this.purystack == 2 and this.puryclock > this.puryiv :
            this.pury()
        elif ret == 0 and this.purystack == 3 :
            this.pury()
        
    def tick(this,rate=0.9):
        this.clock += this.clockoffset
        this.blackclock += this.clockoffset
        this.puryclock += this.clockoffset
        if this.puryclock > this.puryiv :
            this.puryclock -= this.puryiv
            this.purystack += 1
            if this.purystack > 3 + this.light :
                this.purystack = 3 + this.light

        this.takemelee()
        ret = this.takephy()
        this.takemag()
        
        this.puryac(ret)

        this.stclock += this.clockoffset
        if this.stclock > this.stiv :
            this.stclock -= this.stiv
            this.sttaken += this.sttick
            this.st -= this.sttick



    
    #dmg 2 face
    def face(this,time=1):  
        time = int(time / this.clockoffset)
        for i in range(time):
            this.tick(this.srate)
            if this.fout != 0:
                dmg = this.st * this.stdmgrate + 100 - this.srate * 100
                f.write("%d,"%dmg)

    #dmg 2 ironskin
    def iron(this,time = 1):
        times = int(time / this.clockoffset)
        for i in range(times):
            this.tick(this.irate)

            if this.fout != 0:
                dmg = this.st * this.stdmgrate + 100 - this.irate * 100
                print dmg 
                f.write("%d,"%dmg)
    # lock 
    def lock(this,time = 3):
        for i in range(time):
            this.total += 100.0
            this.st += this.irate * 100
            if this.fout != 0:
                dmg = 100 - this.irate * 100
                f.write("%d,"%dmg)

    def pury(this):
        this.avoid += (this.phrate + this.prate) * this.st 
        this.st -= this.prate * this.st
        this.sttick -= this.sttick * this.prate
        this.purystack -= 1



    def showavoid(this):
        if this.prate == 0.65:
            print 'ed',  
        elif this.srate == 0.5:
            print 'ht',
        else :
            print 'bc',
        if this.ring == 1 :
            print 'ring',
        if this.waist ==1:
            print 'waist',
        print this.avoid/this.total
        return this.avoid/this.total

    def getavoid(this):
        return this.avoid/this.total
    def getehp(this):
        return 1/(1-this.avoid/this.total)
    def clean(this):
        this.st = 0
        this.avoid = 0
        this.total = 0


