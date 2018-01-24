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
    e = [ns,gs,bw,qy]
    avelog(Ts,e,Tan)
    ave(Ts,e,Cui)

    e = [ns,gs,fc,mz]
    ave(Ts,e,Tan)
    ave(Ts,e,Cui)



    return 
    e = [bw,jf,wj,qy]
    e = [bw,jf,wj,qy]
    ave(Normala, e, Cui)
    ave(Normala, e, Tan)

    e = [bw,jf,wj,jf]
    ave(Normala, e, Cui)
    ave(Normala, e, Tan)

    return 

if __name__ == "__main__" :
    main()
