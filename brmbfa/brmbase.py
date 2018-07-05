from timeline import Timeline
from timeline import Processor

class Skill(object):
    pass


class Stat(object):
    def __init__(this):
        this.value = 0
        pass
    def __setattr__(this, name, value):
        object.__setattr__(this, name, value)
    def __getattr__(this, name, value):
        object.__getattr__(this, name, value)


class Aura(object):
    pass


class Brmbase(object):
    def __init__(this):
        this.tl = Timeline()

        this.realtime = this.timer(this.p_realtime)

        this.gcd = this.timer(this.p_gcd, (0, 0), 0)
        this.gcd.idle = 1

        this.ks = this.timer(this.p_ks, (0, 6.5), 0)
        this.ks.cd = 0


    
    def timer(this, cb, ti=(0, 0), enable=1):
        timing = ti[0]
        interval = ti[1]
        if not timing and interval:
            timer = this.tl.createp(cb,this.tl.now(),interval)
        else:
            timer = this.tl.createp(cb,timing,interval)
        if enable:
            timer.enable()
        return timer

    def p_gcd(this, p):
        if this.act_gcd() :
            this.idle = 0
            this.gcd.set(0,1)
        else:
            this.idle = 1
            this.gcd.set(0,0)

    def act_gcd(this):
        if not this.ks.cd :
            print 'ks!', this.tl.now()
            this.ks.cd = 1
            this.ks.enable()
            return 1
        else:
            return 0

    def p_realtime(this, p):
        this.act_realtime()

    def act_realtime(this):
        pass


    def p_ks(this, p):
        p.cd = 0
        p.disable()


    def run(this):
        this.gcd.enable()
        this.tl.run(50,0.1)

def main():
    brm = Brmbase()
    brm.run()


if __name__ == "__main__":
    main()
