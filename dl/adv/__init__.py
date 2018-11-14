from core.timeline import *
from core.log import *



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
            return 1

    def ac(this):
        Event(this.name).trigger()

class Adv(object):
    x_status = (0,0)
    log = []
    conf = {}

    def __init__(this,conf):
        tmpconf = {}
        tmpconf.update(this.conf)
        tmpconf.update(conf)
        this.conf = tmpconf
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
        this.x_status = (0,0)
        Event("s1").listener(this.s)
        Event("s2").listener(this.s)
        Event("s3").listener(this.s)


    def x(this): #virtual
        pass

    def ac(this, e):
        this.x()

    def run(this, d = 300):
        this.init()
        Timeline().run(d)

    def think_pin(this, pin):
        if pin in this.conf['think_latency'] :
            latency = this.conf['think_latency'][pin]
        else:
            latency = this.conf['think_latency']['default']
        e = Event('think', this.think).on(now() + latency).pin = pin

    def think(this, e):
        if e.pin == 'sp' and 'sp' in this.conf['al']:
            for i in this.conf['al']['sp']:
                if getattr(this,i).cast():
                    break

        if e.pin == 'x_cancel':
            if 'x5' in this.conf['al'] and this.x_status == (5, 0):
                for i in this.conf['al']['x5']:
                    if getattr(this,i).cast():
                        break
            elif 'x4' in this.conf['al'] and this.x_status == (4, 5):
                for i in this.conf['al']['x4']:
                    if getattr(this,i).cast():
                        break
            elif 'x3' in this.conf['al'] and this.x_status == (3, 4):
                for i in this.conf['al']['x3']:
                    if getattr(this,i).cast():
                        break
            elif 'x2' in this.conf['al'] and this.x_status == (2, 3):
                for i in this.conf['al']['x2']:
                    if getattr(this,i).cast():
                        break
            elif 'x1' in this.conf['al'] and this.x_status == (1, 2):
                for i in this.conf['al']['x1']:
                    if getattr(this,i).cast():
                        break
            #elif this.x_status == (0, 1) and this.conf['al']['x1']:
                #for i in this.conf['al']['x0'] :
                    #getattr(this, i).cast()
        if e.pin == 's' and 's' in this.conf['al']:
            for i in this.conf['al']['s'] :
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
        if this.x_status[1] == 0 :
            time = this.conf["x1_startup"]
            this.idle.timing += time
            if this.x_status[0] == 0:
                this.think_pin('s')
            this.x_status = (0, 1)
            return

        seq = this.x_status[1]
        dmg = this.conf["x%d_dmg"%seq] 
        sp = this.conf["x%d_sp"%seq] 
        e = Event("x%d_missile"%seq, this.missile, \
                now() + this.conf['missile_iv'][seq] )
        e.amount = dmg
        e.samount = sp
        e.on()

        if seq == 5:
            log("x", "x%d"%seq, 0,"-------------------------------------c5")
        else:
            log("x", "x%d"%seq, 0)
        this.think_pin("x_cancel")

        if seq == 5:
            this.x_status = (5, 0)
            time = this.conf["x5_recovery"]
        else:
            this.x_status = (seq, seq+1)
            time = this.conf["x%d_startup"%(seq+1)]
        this.idle.timing += time

    def melee_x(this):
        seq = this.x_status
        dmg = this.conf["x%d_dmg"%seq]
        sp = this.conf["x%d_sp"%seq] 
        log("x", "x%d"%seq, 0)

        this.dmg_make("x%d"%seq, dmg)
        this.charge("x%d"%seq, sp)

    def dmg_make(this, name, count):
        count = count * this.dmg_mod()
        
        if name[0] == "x":
            spgain = this.conf[name[:2]+"_sp"]
            log("dmg", name, count, "%d/%d, %d/%d, %d/%d (+%d)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )
        else:
            spgain = this.conf[name[:2]+"_sp"]
            log("dmg", name, count, "%d/%d, %d/%d, %d/%d (-%d)"%(\
                this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, spgain) )


    def s(this, e):
        func = e.name + '_proc'
        getattr(this, func)(e)
        #if e.name == "s1":
            #this.s1_proc(e)

        seq = this.x_status[0]
        log("cast", e.name, 0,"<cast> %d/%d, %d/%d, %d/%d (%s after c%s)"%(\
            this.s1.charged, this.s1.sp, this.s2.charged, this.s2.sp, this.s3.charged, this.s3.sp, e.name, seq ) )

        this.idle.timing = now() + this.conf[e.name+"_time"]
        this.dmg_make(e.name , this.conf[e.name+"_dmg"])

        this.x_status = (0, 0)
        #this.think_pin("s")

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


if __name__ == "__main__":

    conf = {}
    conf.update( {
        "x_type"      : "ranged" ,

        "x1_dmg"      : 0.98     ,
        "x1_sp"       : 130      ,
        "x1_startup"  : 18/60.0  ,

        "x2_dmg"      : 1.06     ,
        "x2_sp"       : 200      ,
        "x2_startup"  : 33/60.0  ,

        "x3_dmg"      : 1.08     ,
        "x3_sp"       : 240      ,
        "x3_startup"  : 31/60.0  ,

        "x4_dmg"      : 1.56     ,
        "x4_sp"       : 430      ,
        "x4_startup"  : 53/60.0  ,

        "x5_dmg"      : 2.06     ,
        "x5_sp"       : 600      ,
        "x5_startup"  : 64/60.0  ,
        "x5_recovery" : 68/60.0  ,

        "fs_dmg"      : 1.8      ,
        "fs_sp"       : 400      ,
        "fs_startup"  : 42/60.0  ,
        "fs_recovery" : 81/60.0  ,

        "dodge_recovery": 43/60.0,

        "missile_iv"  : [0.7/2, 0.7, 0.7, 0.7, 0.7, 0.7], # fs, c1, c2...
        } )

    conf.update( {
        "s1_dmg"  : 1.61*6   ,
        "s1_sp"   : 2648     ,
        "s1_time" : 167/60.0 ,

        "s2_dmg"  : 2.44*4   ,
        "s2_sp"   : 5838     ,
        "s2_time" : 114/60.0 ,

        "s3_dmg"  : 0        ,
        "s3_sp"   : 0        ,
        "s3_time" : 0        ,
        } )

    conf.update( {
        "think_latency" : {'x_cancel':0.05, 'sp':0.05 , 'default':0.05}
        } )
    al = {
        'sp': [],
        'x5': [],
        'x4': [],
        'x3': [],
        'x2': [],
        'x1': [],
        'x0': [],
        }

    al.update( {
            #'sp': ["s1","s2"],
            'x5': ["s1", "s2"],
            'x4': ["s1", "s2"],
            'x3': ["s1", "s2"],
            'x2': ["s1", "s2"],
            'x1': ["s1", "s2"],
            'x0': ["s1", "s2"],
        } )

    conf['al'] = al

    a = Adv(conf)
    a.run(300)
    logcat(['dmg','x','cast'])
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
            


