
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
    def onattack(this,src):
        pass
    def onhit(this,dst):
        pass
    def onequip(this,src):
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

class bw(Equip):
    stat = {
            'ad':40
            ,'isp':0.25
            }

    onhitdmg = 0
    def onhit(this,target):
        ret = target.takephy(target.hp * 0.08)
        this.onhitdmg += ret
    
class qy(Equip):
    stat = {
            'ad':50
            ,'armbreakp':0.4
    }

