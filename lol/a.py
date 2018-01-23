from base import *

class Normala(Unit):
    def __init__(this,*args,**argv):
        super(Normala,this).__init__(*args,**argv)
        this.isp = 18 * 0.3


class Tan(Target):
    def __init__(this,*args,**argv):
        super(Tan, this).__init__(*args,**argv)
        this.hpmax = 4000
        this.hp = this.hpmax
        this.armbase = 90
        this.arm = 60+80
        this.res = 200

class Cui(Target):
    def __init__(this,*args,**argv):
        super(Cui, this).__init__(*args,**argv)
        this.hpmax = 2000
        this.hp = this.hpmax
        this.armbase = 60
        this.arm = 30
        this.res = 50

def main():
    e = [bw,jf]
    ave(Unit, e, Cui)
    ave(Unit, e, Tan)

    e = [wj,jf]
    ave(Unit, e, Cui)
    ave(Unit, e, Tan)

    return 

if __name__ == "__main__" :
    main()
