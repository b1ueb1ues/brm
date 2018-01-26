from base import *

class Normala(Unit):
    def _init(this):
        this.stat['isp'] = 18 * 0.03

class Ts(Unit):
    def _init(this):
        this.stat['isp'] = 0.474

    def onhit(this,src,dst):
        this.dealmag(this.getstat('ap') * 0.3 + 60,'zyzn') 
        super(Ts,this).onhit(src,dst)



class Tan(Target):
    def _init(this):
        this.stat['hpmax'] = 4000
        this.stat['armbase'] = 90
        this.stat['arm'] = 60+80
        this.stat['res'] = 200

class Cui(Target):
    def _init(this):
        this.stat['hpmax'] = 2000
        this.stat['armbase'] = 60
        this.stat['arm'] = 30
        this.stat['res'] = 50

def main():
    if 0 :
        e = [wj,jf,bw,qy,hq]
        avelog(Normala,e,Tan)
        ave(Normala,e,Cui)
        print ''
        e = [wj,jf,bw,qy,lc]
        ave(Normala,e,Tan)
        avelog(Normala,e,Cui)
        print ''
        return

    e = [gs,bw,ns,qy,sx]
    avelog(Ts,e,Tan)
    ave(Ts,e,Cui)
    print ''
    e = [gs,bw,ns,qy,jf]
    ave(Ts,e,Tan)
    ave(Ts,e,Cui)
    print ''
    return


if __name__ == "__main__" :
    main()
