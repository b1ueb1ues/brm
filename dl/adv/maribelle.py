import adv
import wep.wand


class Maribelle(adv.Adv):
    conf = {}
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
    conf.update(wep.wand.conf)

    def sp_mod(this):
        return 1.05


    def s1_proc(this, e):
        pass
    def s2_proc(this, e):
        pass
    def s3_proc(this, e):
        pass
