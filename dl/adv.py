from timeline import *
from log import *


conf = {
        "x1_dmg"  : 0.98    ,
        "x1_sp"   : 130     ,
        "x1_time" : 15/60.0 ,

        "x2_dmg"  : 1.06    ,
        "x2_sp"   : 200     ,
        "x2_time" : 25/60.0 ,

        "x3_dmg"  : 1.08    ,
        "x3_sp"   : 240     ,
        "x3_time" : 30/60.0 ,

        "x4_dmg"  : 1.56    ,
        "x4_sp"   : 430     ,
        "x4_time" : 52/60.0 ,

        "x5_dmg"  : 2.06    ,
        "x5_sp"   : 600     ,
        "x5_time" : 65/60.0 ,

        "_END":0
        }
print conf

class Adv(object):
    x_status = 1 
    log = []

    def __init__(this,conf):
        this.conf = conf

    def ac(this, e):
        if this.x_status == 1:
            this.x1()
        elif this.x_status == 2:
            this.x2()
        elif this.x_status == 3:
            this.x3()
        elif this.x_status == 4:
            this.x4()
        elif this.x_status == 5:
            this.x5()

    def run(this, d = 10):
        this.idle = Event("idle", this.ac).on()
        Timeline().run(d)

    def charge(this, name, sp):
        log("sp", name, sp)
        pass

    def dmg_mod(this):
        armor = 10
        mod = 5.0/3/armor
        return mod

    def sp_mod(this):
        return 1

    def missile(this,e):
        log("dmg",e.name, e.amount)
        this.charge(e.name, e.samount)

    def range_x(this, seq):
        log("x", "x%d"%seq, 0)
        dmg = this.conf["x%d_dmg"%seq] * this.dmg_mod()
        sp = this.conf["x%d_sp"%seq] * this.sp_mod()
        time = this.conf["x%d_time"%seq]
        this.idle.timing += time

        e = Event("x%d_missile"%seq, this.missile, now()+0.5)
        e.amount = dmg
        e.samount = sp
        e.on()
    
    def melee_x(seq,dmg,sp):
        dmg = this.conf["x%d_dmg"%seq] * this.dmg_mod()
        sp = this.conf["x%d_sp"%seq] * sp_mod()
        log("dmg", "x%d"%seq, dmg)
        this.charge("x%d"%seq, sp)

    def x1(this):
        this.range_x(1)
        this.x_status += 1
    def x2(this):
        this.range_x(2)
        this.x_status += 1
    def x3(this):
        this.range_x(3)
        this.x_status += 1
    def x4(this):
        this.range_x(4)
        this.x_status += 1
    def x5(this):
        this.range_x(5)
        this.x_status = 1
    def sp1(this):
        pass
    def sp2(this):
        pass

a = Adv(conf)
a.run(300)
logcat()

