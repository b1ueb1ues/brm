import random
from timeline import *

random.seed()

class Brm(object):
    m = 0.2
    dodgebase = 0.08
    def __init__(this):
        this.m_stack = 0
        this.hit = 0
        this.miss = 0
        return

    def take_melee(this,e):
        r = random.random()
        dodge = this.dodgebase + this.m * this.m_stack
        if r < dodge:
            #!dodge
            this.m_stack = 0
            this.miss += 1
        else:
            this.m_stack += 1
            this.hit += 1

    def bos(this,e):
        if this.m_stack * this.m + this.dodgebase >= 0.95:
            e.timing += 1.5
            return
        this.m_stack += 1


b = Brm()
b.m = 0.12
b.dodgebase = 0.055
Repeat_event("dt",b.take_melee,1.5)
Repeat_event("bos",b.bos,3)

print "mastery dodge dr_improve"
dr_old = 0
f = open('mastery_dodge.csv','w')
for i in range(8,51):
    b.m = i/100.0
    dsum = 0
    rang = 1000
    for i in range(rang):
        Timeline.run(100000)
        dr = float(b.miss)/(b.hit+b.miss)
        dsum += dr
        #print b.miss, b.hit+b.miss, dr
        b.__init__()
    dr = dsum / rang
    dri = 1-(1-dr)/(1-dr_old)
    ehi = (1-dr_old)/(1-dr)
    dr_old = dr
    print "%.2f :  %.3f (%.4f,%.4f)"%(b.m, dr, dri, ehi)
    f.write( "%.2f,%.4f,%.4f\n"%(b.m, dri,ehi) )

