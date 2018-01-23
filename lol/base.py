from clock import *
import random
from equip import *




class Target(object):
    def __init__(this,clk,src):
        this.hpmax = 2000
        this.hp = this.hpmax
        this.armbase = 90
        this.arm = 60
        this.res = 100
        this.clock = clk
        this.src = src
        this.diein = 0

    def getres(this):
        return this.res

    def getarmtotal(this):
        return this.arm + this.armbase

    def getarm(this):
        return this.arm

    def takephy(this,hit):
        armbreakp = this.src.armbreakp
        armbreak = this.src.armbreak
        realarm = this.getarmtotal() - this.getarm()*armbreakp - armbreak 
        dmgrate = 100.0 / ( realarm + 100.0)
        dmg = hit * dmgrate
        this.hp -= dmg
        if this.hp >= 0:
            return dmg
        else:
            return 0

class Unit(object):
    def __init__(this, clk=0, equip=0, target=0):
        this.base_ad = 100
        this.ad = 0
        this.ap = 0
        this.speedbase = 0.625
        this.isp = 0.4
        this.armbreak = 0
        this.armbreakp = 0
        this.resbreak = 0
        this.resbreakp = 0
        this.crit = 0
        this.critpower = 1

        this.dmgbuff = []

        this.clock = clk
        if equip != 0:
            this.equip = equip[:]
        else:
            this.equip = [bw,jf,wj]

        if target != 0:
            this.target = target
        else:
            this.target = Target(clk,this)


        this.equipstat = {}

        this.aura = []
        this.aurastat = {}

        this.equiponhit = {}
        this.equiponattack = {}

        random.seed()
        this.initialized = 0
        this.hpmax = 2000


    def init(this):
        tmp_equipstat = {}

        for k in range(len(this.equip)):
            i = this.equip[k]
            #instance
            this.equip[k] = i()
            for j in i.stat :
                if j in tmp_equipstat :
                    if '_uniq' in j:
                        pass
                    else:
                        tmp_equipstat[j] += i.stat[j]
                else:
                    tmp_equipstat[j] = i.stat[j]

        #combined uniq
        for i in tmp_equipstat :
            end = i.find('_uniq_')
            if end != -1 :
                name = i[:end]
                if name in this.equipstat :
                    this.equipstat[name] += tmp_equipstat[i]
                else:
                    this.equipstat[name] = tmp_equipstat[i]
            else:
                this.equipstat[i] = tmp_equipstat[i]

        if 'ad' in this.equipstat:
            this.ad += this.equipstat['ad']
        if 'ap' in this.equipstat:
            this.ap += this.equipstat['ap']
        if 'isp' in this.equipstat:
            this.isp += this.equipstat['isp']
        if 'crit' in this.equipstat:
            this.crit += this.equipstat['crit']
        if 'critpower' in this.equipstat:
            this.critpower += this.equipstat['critpower']
        if 'armbreak' in this.equipstat:
            this.armbreak += this.equipstat['armbreak']
        if 'armbreakp' in this.equipstat:
            this.armbreakp += this.equipstat['armbreakp']
        if 'resbreak' in this.equipstat:
            this.resbreak += this.equipstat['resbreak']
        if 'resbreakp' in this.equipstat:
            this.resbreakp += this.equipstat['resbreakp']

        #print this.equipstat

        #onequip callback
        for i in this.equip :
            i.onequip(this)

        this.initialized = 1


    def getad(this):
        return this.ad + this.base_ad

    def getap(this):
        return this.ap

    def getiv(this):
        speed = this.speedbase * (1.0 + this.getisp())
        return 1.0 / speed

    def getisp(this):
        return this.isp

    def getcrit(this):
        return this.crit

    def getcritpower(this):
        return this.critpower

    def onattack(this,src):
        pass

    def onhit(this,dst):
        for i in this.equip :
            i.onhit(dst)


    def attack(this):
        this.onattack(this)
        this.onhit(this.target)
        r = random.random()
        hit = this.getad()
        crit = this.getcrit() 
        if r < crit :
            hit = hit * (1 + this.getcritpower())
        return this.target.takephy(hit)

    class Swing(Proc):
        def tick(this):
            ret = this.host.attack()
            if ret :
                this.host.clock.add(this,this.host.getiv()+this.clock.now)
            else:
                #print 'kill at', this.clock.now
                this.host.target.diein = this.clock.now
                return

    def run(this):
        if this.initialized != 0 :
            print 'dirty'
            return
        if this.clock == 0:
            print 'clock not set'
            return
        this.init()
        this.swing = Unit.Swing(this.clock)
        this.swing.host = this
        this.clock.add(this.swing,0)
        this.clock.run()

    
def ave(someunit, equip, n=100):
    time = 0
    tried = 0
    for i in range(n):
        c = Clock()
        a = someunit(c,equip)
        a.run()
        time += a.target.diein
        tried += 1
    print time/n


def main():
    e = [bw,jf,wj]
    ave(Unit, e)
    e = [jf,jf,wj]
    ave(Unit, e)


if __name__ == "__main__" :
    main()
