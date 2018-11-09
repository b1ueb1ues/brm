from timeline import *
from log import *


conf = {
        "x_type"     : "ranged" ,
        "missile_iv" : 0.5      ,
        "x1_dmg"     : 0.98     ,
        "x1_sp"      : 130      ,
        "x1_time"    : 15/60.0  ,

        "x2_dmg"     : 1.06     ,
        "x2_sp"      : 200      ,
        "x2_time"    : 25/60.0  ,

        "x3_dmg"     : 1.08     ,
        "x3_sp"      : 240      ,
        "x3_time"    : 30/60.0  ,

        "x4_dmg"     : 1.56     ,
        "x4_sp"      : 430      ,
        "x4_time"    : 52/60.0  ,

        "x5_dmg"     : 2.06     ,
        "x5_sp"      : 600      ,
        "x5_time"    : 65/60.0  ,

        }

conf.update(  {
        "sk1_dmg"  : 4     ,
        "sk1_sp"   : 2500  ,
        "sk1_time" : 3     ,

        "sk2_dmg"  : 4     ,
        "sk2_sp"   : 5000  ,
        "sk2_time" : 3     ,

        "sk3_dmg"  : 4     ,
        "sk3_sp"   : 10000 ,
        "sk3_time" : 3     ,
        }
        )

conf.update(  {
        "think_latency" : 0.2   ,
        }
        )

al = {
        'x5': ["sk1", "sk2", "sk3"],

        }

class Skill(object):
    charged = 0
    def __init__(this, name=None, sp=None, ac=None):
        if name:
            this.name = name
        if ac :
            this.ac = ac
        if sp:
            this.sp = sp
    def charge(this,sp):
        this.charged += sp

    def check(this):
        if this.charged >= sp:
            return 1
        else:
            return 0

    def cast(this):
        if not check():
            return 0
        else:
            this.charged = 0
            this.ac()

    def ac(this):
        log("cast", this.name, 0)
        Event(this.name).trigger()

class Adv(object):
    x_status = 1 
    log = []

    def __init__(this,conf):
        this.conf = conf
        this.s1 = Skill("s1")
        this.s2 = Skill("s2")
        this.s3 = Skill("s3")
        Event("s1").listener(this.s)
        Event("s2").listener(this.s)
        Event("s3").listener(this.s)


        if this.conf['x_type']== "ranged":
            this.x = this.range_x
        elif this.conf['x_type']== "melee":
            this.x = this.melee_x

    def x(this): #virtual
        pass

    def ac(this, e):
        this.x()

    def run(this, d = 10):
        this.idle = Event("idle", this.ac).on()
        Timeline().run(d)

    def think_pin(this, pin):
        e = Event('think', this.think).on(now()+this.conf['think_latency']).pin = pin

    def think(this, e):
        if e.pin == 's':

        print 'think()    ', e.timing, e.pin
        pass

    def charge(this, name, sp):
        this.think_pin("sp")
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

        if this.x_status == 5:
            this.x_status = 1
        else:
            this.x_status += 1

    def range_x(this):
        seq = this.x_status
        dmg = this.conf["x%d_dmg"%seq] * this.dmg_mod()
        sp = this.conf["x%d_sp"%seq] * this.sp_mod()
        time = this.conf["x%d_time"%seq]
        this.idle.timing += time

        e = Event("x%d_missile"%seq, this.missile, now()+this.conf['missile_iv'])
        e.amount = dmg
        e.samount = sp
        e.on()

        log("x", "x%d"%seq, 0)
        this.think_pin("x_cancel")

        if this.x_status == 5:
            this.x_status = 1
        else:
            this.x_status += 1

    
    def melee_x(this):
        seq = this.x_status
        dmg = this.conf["x%d_dmg"%seq] * this.dmg_mod()
        sp = this.conf["x%d_sp"%seq] * sp_mod()
        log("x", "x%d"%seq, 0)
        log("dmg", "x%d"%seq, dmg)
        this.charge("x%d"%seq, sp)

        if this.x_status == 5:
            this.x_status = 1
        else:
            this.x_status += 1

    def s(this, e):
        pass

    def s1_proc(this, e):
        pass
    def s2_proc(this, e):
        pass
    def s3_proc(this, e):
        pass

a = Adv(conf)
a.run(300)
logcat()

