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

class wTan(Target):
    def _init(this):
        this.stat['hpmax'] = 4000
        this.stat['armbase'] = 90
        this.stat['arm'] = 60+80+60
        this.stat['res'] = 150

class fTan(Target):
    def _init(this):
        this.stat['hpmax'] = 4000
        this.stat['armbase'] = 90
        this.stat['arm'] = 60
        this.stat['res'] = 230
    def takemag(this,hit,src,name='_'):
        hit = float(hit) * 0.8
        super(fTan,this).takemag(hit,src,name)

class testx(Target):
    def _init(this):
        this.stat['hpmax'] = 2000+400+800+1200*0.75
        this.stat['armbase'] = 90
        this.stat['arm'] = 0
        this.stat['res'] = 50

class testj(Target):
    def _init(this):
        this.stat['hpmax'] = 2000 + 425 + 425
        this.stat['armbase'] = 90
        this.stat['arm'] = 60+60
        this.stat['res'] = 50

        

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
    if 0:
        e = [wj,jf,bw,qy]
        ave(Normala,e,testj)
        ave(Normala,e,testx)
        return

    e = [gs,bw,ns,mz]
    avelog(Ts,e,Tan)
    ave(Ts,e,wTan)
    ave(Ts,e,fTan)
    ave(Ts,e,Cui)
    print ''
    e = [gs,bw,ns,fc]
    ave(Ts,e,Tan)
    ave(Ts,e,wTan)
    ave(Ts,e,fTan)
    ave(Ts,e,Cui)
    print ''
    return


if __name__ == "__main__" :
    main()
