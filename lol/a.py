import clock
import random


class equip(object):
    def __init__(this):
        this.ad = 0
        this.ap = 0
        this.isp = 0
        this.crit = 0
    def onattack(this):
        pass
    def onhit(this):
        pass
    def onequip(this):
        pass


class target(object):
    def __init__(this,el,src):
        this.hpmax = 2000
        this.hp = this.hpmax
        this.armbase = 90
        this.arm = 60
        this.res = 100
        this.el = el
        this.src = src

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
            return 0
        else:
            return 1

class unit(object):
    def __init__(this, el):
        this.ad = 100
        this.ap = 0
        this.speedbase = 0.625
        this.armbreak = 0
        this.armbreakp = 0
        this.resbreak = 0
        this.resbreakp = 0
        this.isp = 0
        this.crit = 0
        this.critpower = 2
        this.equip = []
        this.dst = target(el,this)
        random.seed()
        this.el = el

    def getad(this):
        return this.ad

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

    def onattack(this):
        pass

    def onhit(this):
        pass

    class attackEvent(event.Event):
        def process(this):
            ret = this.src.attack()
            if ret == 0 :
                this.time += this.src.getiv()
                this.src.el.add(this)
            else:
                print this.time
                exit()


    def attack(this):
        this.onattack()
        this.onhit()
        r = random.random()
        hit = this.getad()
        crit = this.getcrit() 
        if r < crit :
            hit = hit * this.getcritpower()
        return this.dst.takephy(hit)

    def run(this):
        this.ae = unit.attackEvent()
        this.ae.src = this
        this.el.add(this.ae)
        this.el.run()

    
        

def main():
    el = event.Eventlist()
    a = unit(el)
    a.run()


if __name__ == "__main__" :
    main()
