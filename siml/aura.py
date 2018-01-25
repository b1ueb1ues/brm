from clock import *

auraindex = {}


class Aura(Proc):
    def __init__(this,clk):
        super(Aura,this).__init__(clk)
        this.enable = 0
        this.duration = 6000
        this._test = 0
        this._init()

        this.host = 0
        this._indexmax = 256
        this.index = 0
    def _init():
        pass

    def getindex(this):
        if this.index >= 0 :
            return this.index
        else :
            return this._indexmax + this.index
    def on(this):
        this.start = this.clock.now
        this.enable = 1
        if this.duration != -1:
            this.clock.add(this,this.start + this.duration)
        this._on()
    def _on(this):
        pass

    def off(this):
        this.enable = 0
        this._off()
    def _off(this):
        pass

    def tick(this):
        if this.clock.now - this.start != this.duration:
            return
        this._test = this.clock.now
        this._tick()
        this.off()
    def _tick(this):
        pass

    def procstat(this,stat):
        pass


def main():
    a = {}
    a[1] = '1'
    a[0] = '0'
    a[255] = '2'
    a[254] = '2'
    for i in a:
        print i,a[i]

if __name__ == "__main__":
    main()
