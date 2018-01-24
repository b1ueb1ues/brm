from clock import *
import random
from equip import *




class Target(object):
    def __init__(this,clk):
        this.stat = {
                'hpmax':2000
                ,'armbase':90
                ,'arm':60
                ,'res':100
                }
        this.clock = clk
        this.diein = 0
        this._init()
        this.hp = this.stat['hpmax']

    def _init(this):
        pass


    def getstat(this,stat):
        if stat in this.stat:
            return this.stat[stat]

    def getarmtotal(this):
        return this.getstat('arm') + this.getstat('armbase')


    def takephy(this,hit,src,name='_'):
        armbreakp = src.getstat('armbreakp')
        armbreak = src.getstat('armbreak')
        realarm = this.getarmtotal() - this.getstat('arm')*armbreakp - armbreak 
        dmgrate = 100.0 / ( realarm + 100.0)
        dmg = hit * dmgrate
        this.hp -= dmg
        this.clock.log("%d: phydmg:%d , hpleft:%d (%s)"%(this.clock.now,dmg,this.hp,name))
        if this.hp >= 0:
            return dmg
        else:
            return 0


    def takemag(this,hit,src,name='_'):
        resbreakp = src.getstat('resbreakp')
        resbreak = src.getstat('resbreak')
        realres = this.getstat('res') - this.getstat('res')*resbreakp - resbreak 
        dmgrate = 100.0 / ( realres + 100.0)
        dmg = hit * dmgrate
        this.hp -= dmg
        this.clock.log("%d: magdmg:%d , hpleft:%d (%s)"%(this.clock.now,dmg,this.hp,name))
        if this.hp >= 0:
            return dmg
        else:
            return 0


class Unit(object):
    def __init__(this, clk=0, equip=0, target=0):
        this.stat = {
                'base_ad':100
                ,'ad':0
                ,'ap':0
                ,'speedbase': 0.625
                ,'isp': 0.4
                ,'armbreak': 0
                ,'armbreakp': 0
                ,'resbreak': 0
                ,'resbreakp': 0
                ,'crit': 0
                ,'critpower': 1
                ,'hpmax':2000
                }

        this.dmgbuff = {}

        this.clock = clk
        if equip != 0:
            this.equip = equip[:]
        else:
            this.equip = [bw,jf,wj]

        if target != 0:
            this.target = target
        else:
            this.target = Target(clk)

        this.equipstat = {}

        this.aura = []
        this.aurastat = {}

        this.equiponhit = {}
        this.equiponattack = {}

        random.seed()
        this._init()
        this.initialized = 0


    def _init(this):
        pass


    def init(this):
        tmp_equipstat = {}

        for k in range(len(this.equip)):
            i = this.equip[k]
            #instance
            this.equip[k] = i(this.clock)
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

        #add static stat together
        for i in this.equipstat:
            this.stat[i] += this.equipstat[i]

        #print this.equipstat

        #onequip callback
        for i in this.equip :
            i.onequip(this)

        this.initialized = 1


    def getaurastat(this,stat):
        ret = 0
        for i in this.aurastat :
            if stat in this.aurastat[i]:
                ret += this.aurastat[i][stat]
        return ret


    def getstat(this,stat):
        ret = 0
        if stat == 'total_ad':
            ret += this.stat['ad'] + this.stat['base_ad']
            return ret

        if stat in this.stat :
            ret += this.stat[stat]

        ret += this.getaurastat(stat)
        return ret


    def gettotalad(this):
        ad = this.getstat('base_ad') + this.getstat('ad')
        return ad


    def getiv(this):
        speed = this.getstat('speedbase') * (1.0 + this.getstat('isp')) 
        if speed > 2.5:
            speed = 2.5
        iv =  1000 / speed
        return iv


    def onattack(this,src,dst):
        for i in this.equip :
            i.onattack(src,dst)


    def onhit(this,src,dst):
        for i in this.equip :
            i.onhit(src,dst)


    def dealphy(this,hit,name='_'):
        for i in this.dmgbuff:
            hit *= this.dmgbuff[i]
        return this.target.takephy(hit,this,name)


    def dealmag(this,hit,name='_'):
        for i in this.dmgbuff:
            hit *= this.dmgbuff[i]
        return this.target.takemag(hit,this,name)


    def attack(this):
        this.onattack(this,this.target)
        this.onhit(this,this.target)
        r = random.random()
        hit = this.gettotalad()
        crit = this.getstat('crit') 
        if r < crit :
            hit = hit * (1 + this.getstat('critpower'))
        return this.dealphy(hit)


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

    
def ave(someunit, equip, target, n=100):
    time = 0
    tried = 0
    for i in range(n):
        c = Clock()
        t = target(c)
        a = someunit(c,equip,t)
        a.run()
        time += a.target.diein
        tried += 1
    print time/n/1000

def avelog(someunit, equip, target, n=100):
    time = 0
    tried = 0
    for i in range(n):
        c = Clock()
        t = target(c)
        a = someunit(c,equip,t)
        a.run()
        time += a.target.diein
        tried += 1
    c.printlog()
    print time/n/1000


def main():
    e = [bw,jf,wj,qy]
    ave(Unit, e, Target)
    e = [jf,bw,qy]
    ave(Unit, e, Target)


if __name__ == "__main__" :
    main()
