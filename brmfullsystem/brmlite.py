#!/usr/bin/python2.7
# -*- encoding:utf8 -*-

from brmbase import *
from cd import *
from aura import *

#brm(talent=['black','light','ht','bc','ed'],equip=['ring','waist','wrist'], \
#            iron = 8, palmcdr = 1.3, haste = 1.3, dodgebase = 0.08, mastery = 0, crit = 0, vers = 0 ):

debug = 2

class brm(brmbase):

    quicksip = 1
    overflowrate = 0

    statisticlist = [
        'totaltank',
        'dtb4st',
        'facetaken',
        'stin',
        'stout',
        'dodge',
        'cast',
        'heal',
        'brewstachetime',
        'overheal',
        'edlevel',
        'stlevel',
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

        if this.mastery != 0:
            r = random.random()
            if r < this.getdodge():
                this.masterystack = 0
                if this.wrist == 1 :
                    this.stackbrew.reduce(1)
                    this.bob.reduce(1)
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

    #########
    # isb
    def castisb(this):
        #print '--cast isb at',this.el.time,this.brewstack.stack()
        ret =this.stackbrew.cast()
        if ret != 0:
            this.isb.cast()
            this.pury(rate=0.05,src='quicksip')
            if 't20' in this.equip:
                this.gift()

            #print '-isbcast----',this.el.time
            this.brewstachebuff.cast()
            #print 'cast isb at',this.now(),'buff at',this.isb.time()
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
                
    class Brewstachebuff(aura):
        starttime = 0
        duration = 4.5
        def startprocess(this,time):
            this.value = 0.1
            this.starttime = time
        def endprocess(this,time):
            bs = this
            brm = bs.src
            bs.value = 0
            brm.brewstachetime.time += (time - bs.starttime)
        def refreshprocess(this,time):
            super(brm.Brewstachebuff,this).refreshprocess(time)
            bs = this
            bm = this.src
            bm.brewstachetime.time += (time - bs.starttime)
            bs.starttime = time

    class Edbuff(aura):
        starttime = 0
        duration = 6
        def startprocess(this,time):
            ed = this
            brm = ed.src
            if brm.st / brm.hpmax > 0.6:
                ed.value = (ed.value * ed.last() + 0.2*6) / 6
            elif brm.st / brm.hpmax > 0.3:
                ed.value = (ed.value * ed.last() + 0.2 * 2/3 * 6) / 6
            else :
                ed.value = (ed.value * ed.last() + 0.2 * 1/3 * 6) / 6
            ed.starttime = time

        def refreshprocess(this,time):
            ed = this
            bm = ed.src
            if bm.st / bm.hpmax > 0.6:
                ed.value = float(ed.value * ed.last())/6 + 0.2
            elif bm.st / bm.hpmax > 0.3:
                ed.value = float(ed.value * ed.last())/6 + 0.2/3*2
            else :
                ed.value = float(ed.value * ed.last())/6 + 0.2/3

            tmp = bm.edlevel.__getattr__('percent_%d'%(ed.value*100)) 
            tmp += (time - ed.starttime)
            ed.starttime = time
            super(brm.Edbuff,this).refreshprocess(time)



        def endprocess(this,time):
            ed = this
            brm = ed.src
            tmp = brm.edlevel.__getattr__('percent_%d'%(ed.value*100)) 
            tmp += (time - ed.starttime)
            ed.value = 0


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


    ##############
    # brews
    class Bobcd(cd):
        cooldown = 90
        def endprocess(this,time):
            this.src.cast.bob += 1
            brm = this.src
            stack,stackmax = brm.stackbrew.stack()
            for i in range(stack):
                brm.castisb()
            brm.stackbrew.setstack(brm.brewstackmax-1,brm.brewstackmax)
            brm.stackbrew.reduce(21)
            this.cast()
            #print '--next bob at',this.time()


    class Brewstack(stack):
        _stack = 3
        _stackmax = 3
        def reduce(this,offset=1):
            super(brm.Brewstack,this).reduce(offset)
            if this._stack >= this._stackmax - 1 :
                if this.last() < this.src.kscdr + 6 :
                    this.src.pury()
                    this.src.cast.pb += 1
                    this.cast()


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
                #print 'cast pb at',this.el.time
                pass
            #    tmp = brm.lagev()
            #    tmp.time = time + 

            #    this.src.cast.pb += 1
            #    this.src.pury()
            #    this.cast()
        def endprocess(this,time):
            #print 'cast isb(brewmax) at',this.now()
            this.src.castisb()

    def gift(this):
        r = random.random()
        h = 0
        celeh = 0
        if r < this.overflowrate :
            h = this.ap * 7.5
        else:
            h = this.ap * 15
        r = random.random()
        if r < this.crit :
            h += h
        r = random.random()
        this.getheal(h,'gift')


    def getheal(this,amount,src='ext'):
        h = amount
        s_h = this.heal.__getattr__(src)
        s_ch = this.heal.__getattr__('cele_'+src)
        s_oh = this.overheal.__getattr__(src)
        s_coh = this.overheal.__getattr__('cele_'+src)


        this.hp += h
        if this.hp > this.hpmax:
            oh = this.hp - this.hpmax
            s_oh += oh
            s_h += (h - oh)
            this.hp = this.hpmax
        else :
            s_h += h

        r = random.random()
        if r < this.crit:
            celeh = h * 0.65

            this.hp += celeh
            if this.hp > this.hpmax:
                oh = this.hp - this.hpmax
                s_coh += oh
                s_ch += (celeh - oh)
                this.hp = this.hpmax
            else :
                s_ch += h






    def pury(this,rate=-2,src='pb'):
        if rate == -2 :
            #print '-pbcast----',this.el.time
            bm = this
            bm.brewstachebuff.cast()
            if bm.ed != 0:
                bm.edbuff.cast()
            if this.quicksip != 0:
                this.isb.delay(1)
        brmbase.pury(this,rate,src)

    
    laststleveltime = 0
    def gethaste(this):
        stpercent = this.st / this.hpmax
        if stpercent > 0.6 :
            stlevel = 'h'
        elif stpercent > 0.3 :
            stlevel = 'm'
        elif this.st != 0 :
            stlevel = 'l'
        else :
            stlevel = 'nil'
        tmp = this.stlevel.__getattr__(stlevel)
        tmp += this.now() - this.laststleveltime
        this.laststleveltime = this.now()

	if this.ht != 0 :
	    if stpercent > 0.6 :
		return this.haste * 1.15
	    elif stpercent > 0.3 :
		return this.haste * 1.1
	    elif this.st != 0 :
		return this.haste * 1.05
	    else :
		return this.haste
	else:
	    return this.haste

    def getdodge(this):
        return this.dodgebase + this.masterystack * this.mastery + this.brewstachebuff.value + this.edbuff.value


    def init(this):
        super(brm,this).init()
        this.init = 0

        this.staggerev = brm.StaggerEv(this.el)

        #this.ch = brm.changehaste(this.el)

        this.ap = this.agi * (1+this.mastery) * 1.05
        
        this.isbduration = 9
        this.isb = brm.ISBbuff(this,duration=this.isbduration)

        #this.ironev = brm.IronEv(this.el)

        this.gm()


        this.ks = brm.Kegcd(this,8,1)
        this.tp = brm.Palmcd(this,5,1)
        this.bob = brm.Bobcd(this)
        this.stackbrew = brm.Brewstack(this,21,1)
        this.stackbrew.setstack(this.brewstack,this.brewstackmax)
        this.brewstachebuff = brm.Brewstachebuff(this)

        this.castisb()
        this.ks.cast()
        this.tp.cast()
        this.bob.cast()


        this.edbuff = brm.Edbuff(this)
        if 'ed' in this.talent:
            this.ed = 1


        this.init = 1

    def __init__(this,**argv):
        super(brm,this).__init__(**argv)


    def getavoid(this):
        if this.noiron != 0:
            return "%.4f|%d"%(brmbase.getavoid(this),this.noiron)
        return "%.5f\t"%(brmbase.getavoid(this))


    def showavoid(this):
        print '\n################'
        print '## showunit test'
        this.totaltank.showunit()
        print this.totaltank.getv()



def main():
    c = brm(stat=[25,25,0,30],talent=['ht'],equip=['t20','4t','ring'])
    c.run(100000)
    c.showavoid()
    return
    a = brm(stat=[25,25,0,30],talent=['ed'],equip=['4t','ring'])
    a.run(100000)
    a.showavoid()
    return
    b = brm(stat=[25,30,0,20],talent=['ht'],equip=['4t','ring'])
    b.run(100000)
    b.showavoid()

    exit()

    b = brm(stat=[25,30,0,20],talent=['ht'],equip=['4t','ring','waist'])
    c = brm(stat=[25,30,0,20],talent=['ht'],equip=['4t','wrist','waist'])
    a.run(100000)
    a.showavoid()
    b.run(100000)
    b.showavoid()
    c.run(100000)
    c.showavoid()


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
