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
    giftcount = 0
    fbmastery = 1
    bsmastery = 1
    mode = 'gm'
    ver = 'ptr'
#    facepalm = 0.4

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
            hpb4 = this.src.hp
            this.src.takestdmg()
            if this.src.hp < this.threashold :
                this.src.paladin()
            if this.src.hp < this.threashold2 :
                if hpb4 > this.threashold2:
                    this.src.gift(src='od')
            #print this.src.gethaste()
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

    def obtaingift(this,dmg):
        this.giftcount += dmg
        if this.giftcount > this.hpmax:
            this.gift()
            this.giftcount = 0

    def takephydmg(this,dmg=4000000):
        this.totaltank.takephydmg += dmg
        dmg -= dmg * this.armorrate
        
        if this.ironskin == 1 :
            rate = this.irate
        else :
            rate = this.srate

        this.dtb4st.takephydmg += dmg
        this.obtaingift(dmg)
        this.stin.takephydmg += rate * dmg
        this.facetaken.takephydmg += dmg * (1-rate)
        this.hp -= dmg * (1-rate)

        this.st += rate * dmg
        this.sttick = this.st * this.stdmgrate

    def takemagicdmg(this,dmg=400000):
        if this.ironskin == 1 :
            rate = this.irate * 0.7
        else :
            rate = this.srate * 0.7
        this.totaltank.takemagicdmg += dmg
        this.dtb4st.takmagicdmg += dmg
        this.obtaingift(dmg)
        this.stin.takmagicdmg += dmg * rate
        this.facetaken.takmagicdmg += dmg * (1-rate)
        this.hp -= dmg * (1-rate)

        this.st += rate * dmg
        this.sttick = this.st * this.stdmgrate

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
        this.obtaingift(dmg)
        this.stin.takemelee += dmg * rate
        this.facetaken.takemelee += dmg * (1-rate)
        this.hp -= dmg * (1-rate)
        this.st += rate * dmg
        this.sttick = this.st * this.stdmgrate

        this.masterystack += 1
   #}takemelee

    def basepury(this,rate=-2,src='pb'):
        if rate == -2 :
            prate = this.prate
        else :
            prate = rate

        a = this.stout.gets(src) 
        a += this.st * prate
        #print this.el.time,this.st,this.st * this.prate
        if rate == -2 and this.phrate != 0 :
            #print this.phrate
            #this.heal.waist += this.phrate * this.st 
            this.getheal(amount=this.phrate*this.st,src='waist')
        this.st -= this.st * prate
        this.sttick -= this.sttick * prate


    def gm(this):
        this.takemeleeev = brm.TakeMeleeEv(this.el,repeat = 2)
        this.takemeleeev.dmg = 8000000
        #this.takemeleeev = brm.TakeMeleeEv(this.el,repeat = 1.5)
        #this.takemeleeev.dmg = 1000000
        #this.armorrate = 0
        pass

    def gd(this):
        this.takemeleeev = brm.TakeMeleeEv(this.el,repeat = 1)
        this.takemeleeev.dmg = 10000000
        #this.takemeleeev = brm.TakeMeleeEv(this.el,repeat = 1.5)
        #this.takemeleeev.dmg = 1000000
        #this.armorrate = 0
        pass

    def krosus(this):
        this.takephyev = brm.TakePhyEv(this.el,repeat = 10)
        this.takemagev = brm.TakeMagEv(this.el,repeat = 1)
        this.takemeleeev = brm.TakeMeleeEv(this.el,repeat = 1.5)
        pass

    def star(this):
        this.takemagev = brm.TakeMagEv(this.el,repeat = 2.5)
        this.takemagev.dmg = 3000000
        pass
    ###########
    # fbbs
    class FBEv(RepeatEvent):
        repeat = 15
        def process(this):
            this.src.masterystack+=this.src.fbmastery
            this.src.cast.fb += 1

    class BSEv(RepeatEvent):
        repeat = 5
        def process(this):
            this.src.masterystack+=this.src.bsmastery
            this.src.cast.bs += 1


    #########
    # isb
    def castisb(this):
        #print '--cast isb at',this.el.time,this.brewstack.stack()
        ret =this.stackbrew.cast()
        if ret != 0:
            this.isb.cast()
            this.pury(rate=0.05,src='quicksip')
            if '2t20' in this.equip or '4t20' in this.equip:
                this.gift(src='2t20')

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

    class Kegcd(Cd):
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
    class Palmcd(Cd):
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
    class Bobcd(Cd):
        cooldown = 90
        def endprocess(this,time):
            this.src.cast.bob += 1
            bm = this.src
            stack,stackmax = bm.stackbrew.stack()
            for i in range(stack):
                bm.castisb()
            #bm.stackbrew.setstack(bm.brewstackmax,bm.brewstackmax)
            bm.stackbrew.full()
            #this.reduce(21)
            this.cast()
            ##print '--next bob at',this.time()


    def castpb(this):
        this.cast.pb += 1
        this.pury()
        this.stackbrew.cast()
        if '2t20' in this.equip or '4t20' in this.equip :
            this.gift(src='2t20')

    class Brewstack(Stack):
        _stack = 3
        _stackmax = 3
        def reduce(this,offset=1):
            super(brm.Brewstack,this).reduce(offset)
            if this._stack >= this._stackmax - 1 :
                if this.last() < this.src.kscdr + 6 :
                    this.src.castpb()
#                    this.src.pury()
#                    this.src.cast.pb += 1
#                    this.cast()


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

    class PaladinEv(RepeatEvent):
        repeat = 8
        def process(this):
            if this.src.hp < this.src.hpmax/2 :
                this.src.paladin()

    dc = 0
    def paladin(this):
        amount = 0
        class healev(Event):
            def process(this):
                this.src.getheal(this.amount)
        tmpev = healev()
        tmpev.time = this.now() + 1.5
        if this.hp < 0 :
            this.dc += 1
            print '----dead',this.dc
            tmpev.amount = this.hpmax/2 - this.hp
        else :
            #tmpev.amount = (this.hpmax - this.hp)/2
            tmpev.amount = 1000000
        tmpev.addto(this.el)


    def gift(this,src='origin'):
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
        this.getheal(h,'gift_'+src)
        if '4t20' in this.equip:
            this.pury(rate=0.05,src='4t20')


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
        this.basepury(rate,src)

    
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

        #this.ap = this.agi * (1+this.mastery) * 1.05

        if this.mode == 'gm':
            this.gm()
        elif this.mode == 'star':
            this.star()

        this.staggerev = brm.StaggerEv(this.el)
        this.staggerev.threashold = this.hpmax * 0.5
        this.staggerev.threashold2 = this.hpmax * 0.35


       # this.bsmastery = 0
       # this.fbmastery = 0
        if this.ver == 'ptr':
            if this.bsmastery != 0:
                this.bsev = brm.BSEv(this.el,withhaste=1)
            if this.fbmastery != 0 :
                if 'chest' in this.equip:
                    this.fbev = brm.FBEv(this.el ,repeat = 8,withhaste=1)
                else :
                    this.fbev = brm.FBEv(this.el ,repeat = 15)
        #cd
        this.ks = brm.Kegcd(this,8,1)
        this.tp = brm.Palmcd(this,4,1)
        this.bob = brm.Bobcd(this)
        this.stackbrew = brm.Brewstack(this,21,1)
        this.stackbrew.setstack(this.brewstack,this.brewstackmax)
        #buff
        this.brewstachebuff = brm.Brewstachebuff(this)
        this.isbduration = 9
        this.isb = brm.ISBbuff(this,duration=this.isbduration)
        this.edbuff = brm.Edbuff(this)
        if 'ed' in this.talent:
            this.ed = 1

        this.castisb()
        this.ks.cast()
        this.tp.cast()
        this.bob.cast()

        #this.paladinev = brm.PaladinEv(this.el)

        this.init = 1

    def __init__(this,**argv):
        super(brm,this).__init__(**argv)


    def getavoid(this):
        if this.noiron != 0:
            return "%.4f|%d"%(brmbase.getavoid(this),this.noiron)
        return "%.5f\t"%(brmbase.getavoid(this))


   # def showavoid(this):
   #     print '\n################'
   #     print '## showunit test'
   #     this.totaltank.showunit()
   #     print this.totaltank.getv()

    def getehr(this):
        return this.heal.ext.value

    def getehrr(this):
        ehr = this.getehr()
        return 1 - ehr / this.totaltank.value

    def showavoid(this):
        print 'stat\t',this.stat
        print 'talent\t',this.talent
        print 'equip\t',this.equip
#
        avoidance = this.getehrr()
        print '----------------------------'
        print ' ehr ->| %.4f%% |<- reduced'%(avoidance*100)
        print '----------------------------'

        print 'melee>_'
        print 'totaltank>_',this.totaltank
        for i in this.totaltank.srcs :
            print '\t',i,this.totaltank.srcs[i]
        if this.mastery != 0 and this.totaltank.takemelee.count != 0:
            print "\tdodge %.2f%%"%(float(this.dodge.takemelee.count)*100/this.totaltank.takemelee.count)
        print '\ndmgtaken b4st>_',this.dtb4st
        for i in this.dtb4st.srcs :
            print '\t',i,this.dtb4st.srcs[i]
        print '\nstagger in>_'
        for i in this.stin.srcs :
            print '\t',i,this.stin.srcs[i]
        print '\nstagger out>_'
        for i in this.stout.srcs :
            print '\t',i,this.stout.srcs[i],'(%.2f%%)'%(this.stout.srcs[i].value/this.stout.value*100)
        print '\nheal>_',this.heal,' | overheal',this.overheal,'(%.2f%%)'%(100*this.overheal.value/(this.heal.value+this.overheal.value))
        cele = []
        celesum = 0
        gift = []
        giftsum = 0
        for i in this.heal.srcs :
            if 'cele_' in i:
                cele.append(this.heal.srcs[i])
                celesum += this.heal.srcs[i].value
                continue
            if 'gift_' in i :
                gift.append(this.heal.srcs[i])
                giftsum += this.heal.srcs[i].value
                continue
            print '\t',i,this.heal.srcs[i],'(%.2f%%) | %d hit'%(this.heal.srcs[i].value/this.heal.value*100,this.heal.srcs[i].count),
            if i in this.overheal.srcs :
                print ' | overheal %s(%.2f%%)'%(this.overheal.srcs[i],100*this.overheal.srcs[i].value/(this.overheal.srcs[i].value+this.heal.srcs[i].value))
        if celesum > 1000000:
            celesumstr = '%.2f'%(celesum/1000000) + 'm'
        elif celesum > 10000:
            celesumstr = '%.2f'%(celesum/10000) + 'w'
        else :
            celesumstr = '%.2f'%celesum
        if giftsum > 1000000:
            giftsumstr = '%.2f'%(giftsum/1000000) + 'm'
        elif giftsum > 10000:
            giftsumstr = '%.2f'%(giftsum/10000) + 'w'
        else :
            giftsumstr = '%.2f'%giftsum
        if cele != []:
            print '\tcele',celesumstr,'(%.2f%%)'%(celesum/this.heal.value*100)
            for i in cele:
                o = this.overheal.srcs[i.getsname()].value
                h = i.value
                ohpercent = o / (o + h) * 100
                print '\t\t',i.getsname(),i,'|',i.count,'hits','| overheal %s(%.2f%%)'%(this.overheal.srcs[i.getsname()],ohpercent)
        if gift != []:
            print '\tgift',giftsumstr,'(%.2f%%)'%(giftsum/this.heal.value*100)
            for i in gift:
                o = this.overheal.srcs[i.getsname()].value
                h = i.value
                ohpercent = o / (o + h)
                print '\t\t',i.getsname(),i,'|',i.count,'hits','| overheal %s(%.2f%%)'%(this.overheal.srcs[i.getsname()],ohpercent)


        print '\ncast>_'
        for i in this.cast.srcs :
            if i in ['isb','pb','bob']:
                continue
            print '\t',i,this.cast.srcs[i].count
        print '\tbrew',this.cast.isb.count+this.cast.pb.count,'+',this.cast.bob.count
        print '\t\tpb',this.cast.pb.count
        print '\t\tisb',this.cast.isb.count
        print '\t\tbob',this.cast.bob.count
        print '\nstaggerlevel>_'
        for i in this.stlevel.srcs :
            print '\t',i,'%.2f%%'%(this.stlevel.srcs[i].value/this.stlevel.value*100)
        print '\nbrewstachetime>_'
        for i in this.brewstachetime.srcs :
            print '\t',i,'%.2f%%'%(this.brewstachetime.srcs[i].value/this.simctime*100)

        return avoidance



def main():
    c = brm(stat=[25,30,0,20],talent=['ht'],equip=['4t19','ring','waist'])
    c.mode = 'gm'
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
