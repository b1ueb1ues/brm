class Proc(object):
    def __init__(this,clk):
        this.clock = clk
        this.iv = clk.iv

    def tick(this):
        pass
        
class Aura(Proc):
    def __init__(this):
        super(Aura,this).__init__(clk)
        this.enable = 0
        this.maxtime = 1

    def on(this):
        this.start = this.clock.now
        this.enable = 1

    def off(this):
        this.enable = 0



class Clock(object):
    def __init__(this):
        this.now = 0.0
        this.longest = 9999
        this.iv = 0.001
        this.proc = []

    def run(this):
        if this.now <= this.longest :
            for i in this.proc :
                i.tick()
            this.now += this.iv

    def stop(this):
        this.longest = this.now


