from clock import *
from aura import *
class Equip(object):
    stat = {
            'ad' : 0
            ,'ap' : 0 
            ,'isp' : 0 
            ,'crit' : 0 
            ,'critpower' : 0 
            ,'armbreak' : 0 
            ,'armbreakp' : 0 
            ,'resbreak' : 0 
            ,'resbreakp' : 0 
            }
    def onattack(this,src,dst):
        pass
    def onhit(this,src,dst):
        pass
    def onequip(this,src):
        pass
    def __init__(this,clock = 0):
        this.clock = clock
        this._init()
    def _init(this):
        pass

class wj(Equip):
    stat = {
            'ad':70
            ,'crit':0.2
            ,'critpower_uniq_wj':0.5
            }
class jf(Equip):
    stat = {
            'isp':0.4
            ,'crit':0.3
            }
    def onhit(this,src,dst):
        src.dealphy(15,'jf')

class lc(Equip):
    stat = {
            'isp':0.45
            ,'crit':0.3
            }

class sx(Equip):
    def _init(this):
        this.rb = 1
    stat = {
            'isp':0.40
            ,'ad':25
            }
    def onhit(this,src,dst):
        if this.rb :
            this.rb = 0
            dmg = src.getstat("base_ad") * 2
            src.dealphy(dmg,'sx')

class wy(Equip):
    stat = {
            'ap':80
            }
class xs(Equip):
    stat = {
            'hpmax':400
            ,'base_ad':50
            }

class bw(Equip):
    stat = {
            'ad':40
            ,'isp':0.25
            }

    onhitdmg = 0
    def onhit(this,src,target):
        ret = src.dealphy(target.hp * 0.08,'bw')
        this.onhitdmg += ret
    
class qy(Equip):
    stat = {
            'ad':50
            ,'armbreakp':0.35
    }
    def onequip(this,src):
        dmgbuff = int((src.target.getstat('hpmax') - src.getstat('hpmax')) / 200) * 0.2 + 1
        if dmgbuff > 1.2:
            dmgbuff = 1.2
        src.dmgbuff[this.__class__] = dmgbuff 


class qy2(Equip):
    stat = {
            'ad':50
    }

class mz(Equip):
    stat = {
            'ap':120
            }
    class mzaura(Aura):
        def _init(this):
            this.index = 256
        def procstat(this,name,value):
            if name == 'ap':
                return value * 1.3
            return value
        def _on(this):
            this.host.addaura('mz',this)

    def onequip(this,src):
        this.mzaura = mz.mzaura(this.clock)
        this.mzaura.host = src
        this.mzaura.on()

class ns(Equip):
    stat = {
            'ap':80
            ,'isp':0.5
            }
    def onhit(this,src,dst):
        src.dealmag(15+src.getstat('ap')*0.15,'ns')

class ns2(Equip):
    stat = {
            'ap':80
            ,'isp':0.5
            }
class fc(Equip):
    stat = {
            'ap':70
            ,'resbreakp':0.4
            }
class gs(Equip):
    stat = {
            'ad':35
            ,'isp':0.25
            ,'ap':50
            }
    def _init(this):
        #this.gsaura = gs.gsaura(this.clock)
        this.gsaura = 0
        this.rage = 0
        this._test = 0


    def onhit(this,src,dst):
        return src.dealmag(15,'gs')
        

    def onattack(this,src,dst):
        if this.gsaura :
            this.gsaura.refresh()
        else:
            this.gsaura = gs.gsaura(this.clock)
            this.gsaura.host = src
            this.gsaura.on()
        if this.gsaura.stack >= 6:
            if this.rage == 1:
                this.rage = 0
                this._test +=1
                src.onhit(src,dst)
            else:
                this.rage = 1

    class gsaura(Aura):
        def _init(this):
            this.stack = 0
            this.stat = {}
            this.duration = 5000
            this.host = 0
            this.index = 1

        def refresh(this):
            this.clock.rm(this,this.end)
            this.on()

        def _on(this):
            if this.stack < 6:
                this.stack += 1
            this.stat['ad'] = this.stack*3
            this.stat['ap'] = this.stack*4
            this.stat['isp'] = this.stack*0.08
            this.host.addaura('gs',this)

        def procstat(this,name,value):
            ret = value
            if name in this.stat:
                ret = value + this.stat[name]
            return ret

        def _off(this):
            this.stat = {}
            this.rage = 0
            this.host.rmaura('gs')

class hq(Equip):
    stat = {
            'ad':40
            ,'hpmax':400
            }
    def _init(this):
        this.hqaura = hq.hqaura(this.clock)

    class hqaura(Aura):
        def _init(this):
            this.stack = 0
            this.stat = {}
            this.duration = 6000
            this.host = 0
            this.index = 1

        def refresh(this):
            this.clock.rm(this,this.end)
            this.on()

        def on(this):
            if this.stack < 6:
                this.stack += 1
            this.stat['arm'] = float(this.stack)*0.04

            if this.enable :
                this.clock.mv(this,this.end,this.clock.now+this.duration)
                this.start = this.clock.now
                this.end = this.start + this.duration
            else:
                this.host.addaura('hq',this)
                this.start = this.clock.now
                this.end = this.start + this.duration
                if this.duration != -1:
                    this.clock.add(this,this.end)

            this.enable = 1

        def procstat(this,name,value):
            ret = value
            if name in this.stat:
                ret = value * (1.0 - this.stat[name])
            return ret

        def _off(this):
            this.stat = {}
            this.rage = 0
            this.host.rmaura('hq')

    def onhit(this,src,dst):
        this.hqaura.host = dst
        this.hqaura.on()

