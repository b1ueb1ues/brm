from timeline import *
from log import *


conf = {}
conf.update( {
        "x_type"     : "ranged" ,

        "missile_iv" : [0.5,0.5,0.5,1.0,1.5]  ,

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
        )




conf.update(  {
        "s1_dmg"  : 1.61*6,
        "s1_sp"   : 2648  ,
        "s1_time" : 3     ,

        "s2_dmg"  : 2.44*4,
        "s2_sp"   : 5838  ,
        "s2_time" : 3     ,

        "s3_dmg"  : 0     ,
        "s3_sp"   : 10000 ,
        "s3_time" : 0     ,

        }
        )

conf.update(  {
    "think_latency" : {'x_cancel':0.2, 'sp':0.05 , 'default':0.05}
        }
        )
al = {
        'sp': [],
        'x5': [],
        'x4': [],
        'x3': [],
        'x2': [],
        'x1': [],
        'x0': [],
        }

al.update({
        #'sp': ["s1","s2"],
        'x5': ["s1","s2"],
        'x4': ["s1","s2"],
        'x3': ["s1","s2"],
        'x2': ["s1","s2"],
        'x1': ["s1","s2"],
        'x0': ["s1","s2"],
        })

conf['al'] = al

class Skill(object):
    charged = 0
    sp = 0
    def __init__(this, name=None, sp=None, ac=None):
        this.charged = 0
        if name:
            this.name = name
        if ac :
            this.ac = ac
        if sp:
            this.sp = sp
    def charge(this,sp):
        this.charged += sp
        #if this.charged > this.sp:
            #this.charged = this.sp

    def check(this):
        if this.charged >= this.sp:
            return 1
        else:
            return 0

    def cast(this):
        if not this.check():
            return 0
        else:
            this.charged = 0
            this.ac()

    def ac(this):
        Event(this.name).trigger()

class Adv(object):
    x_status = 1 
    log = []

    def __init__(this,conf):
        this.conf = conf
        this.s1 = Skill("s1",this.conf["s1_sp"])
        this.s2 = Skill("s2",this.conf["s2_sp"])
        this.s3 = Skill("s3",this.conf["s3_sp"])

        if this.conf['x_type']== "ranged":
            this.x = this.range_x
        elif this.conf['x_type']== "melee":
            this.x = this.melee_x

    def init(this):
        Timeline().reset()
        this.idle = Event("idle", this.ac).on()
        Event("s1").listener(this.s)
        Event("s2").listener(this.s)
        Event("s3").listener(this.s)


    def x(this): #virtual
        pass

    def ac(this, e):
        this.x()

    def run(this, d = 10):
        this.init()
        Timeline().run(d)

    def think_pin(this, pin):
        if pin in this.conf['think_latency'] :
            latency = this.conf['think_latency'][pin]
        else:
            latency = this.conf['think_latency']['default']
        e = Event('think', this.think).on(now() + latency).pin = pin

    def think(this, e):
        if e.pin == 'sp':
            for i in this.conf['al']['sp']:
                getattr(this,i).cast()

        if e.pin == 'x_cancel':
            if this.x_status == 5 and this.conf['al']['x5']:
                for i in this.conf['al']['x5']:
                    getattr(this,i).cast()
            if this.x_status == 4 and this.conf['al']['x4']:
                for i in this.conf['al']['x4']:
                    getattr(this,i).cast()
            if this.x_status == 3 and this.conf['al']['x3']:
                for i in this.conf['al']['x3']:
                    getattr(this,i).cast()
            if this.x_status == 2 and this.conf['al']['x2']:
                for i in this.conf['al']['x2']:
                    getattr(this,i).cast()
            if this.x_status == 1 and this.conf['al']['x1']:
                for i in this.conf['al']['x1']:
                    getattr(this,i).cast()

        if e.pin == 's':
            for i in this.conf['al']['x0'] :
                getattr(this, i).cast()

    def charge(this, name, sp):
        sp = sp * this.sp_mod()
        this.s1.charge(sp)
        this.s2.charge(sp)
        this.s3.charge(sp)
        this.think_pin("sp")
        log("sp", name, sp,"%d/%d, %d/%d, %d/%d"%(\
            this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp) )

    def dmg_mod(this):
        armor = 10
        mod = 5.0/3/armor
        return mod

    def sp_mod(this):
        return 1

    def missile(this,e):
        this.dmg_make(e.name, e.amount)
        this.charge(e.name, e.samount)


    def range_x(this):
        seq = this.x_status
        dmg = this.conf["x%d_dmg"%seq] 
        sp = this.conf["x%d_sp"%seq] 
        time = this.conf["x%d_time"%seq]
        this.idle.timing += time

        e = Event("x%d_missile"%seq, this.missile, now()+this.conf['missile_iv'][seq-1])
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
        dmg = this.conf["x%d_dmg"%seq]
        sp = this.conf["x%d_sp"%seq] 
        log("x", "x%d"%seq, 0)

        this.dmg_make("x%d"%seq, dmg)
        this.charge("x%d"%seq, sp)

        if this.x_status == 5:
            this.x_status = 1
        else:
            this.x_status += 1

    def dmg_make(this, name, count):
        count = count * this.dmg_mod()
        log("dmg", name, count)


    def s(this, e):
        func = e.name + '_proc'
        getattr(this, func)(e)
        #if e.name == "s1":
            #this.s1_proc(e)

        log("cast", e.name, 0,"%d/%d, %d/%d, %d/%d"%(\
            this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp) )

        this.idle.timing = now() + this.conf[e.name+"_time"]
        this.dmg_make(e.name , this.conf[e.name+"_dmg"])


        this.x_status = 1
        this.think_pin("s")

    def s1_proc(this, e):
        pass

    def s2_proc(this, e):
        pass

    def s3_proc(this, e):
        pass


def sum_dmg():
    l = logget()
    dmg_sum = {'x':0, 's':0}
    for i in l:
        if i[1] == 'dmg':
            dmg_sum[i[2][0]] += i[3]

    total = 0
    for i in dmg_sum:
        total += dmg_sum[i]
    dmg_sum['total'] = total
    print dmg_sum


a = Adv(conf)
a.run(300)
logcat()
sum_dmg()


logreset()
conf['al'] = {
        'sp': ["s1","s2"],
        'x5': [],
        'x4': [],
        'x3': [],
        'x2': [],
        'x1': [],
        'x0': [],
        }

a = Adv(conf)
a.run(300)
sum_dmg()
        

