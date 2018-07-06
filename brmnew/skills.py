from timeline import Timeline
import time

class Skill(object):
    def __init__(this, tl, src=0, dst=0):
        this.tl = tl
        this.cd = 8
        this.stackmax = 3
        this.stack = this.stackmax

        this.charge = 0
        this.tick = this.tl.newevent(this.p_tick)

        this.charging = 0


    def haste(this):
        return 0

    def cast(this):
        if this.stack >= 1:
            this.stack -= 1
            if not this.charging :
                this.charging = 1
                this.tick.enable(this.tl.now()+this.cd)
            return 0
        else:
            return this.cd - this.charge

    def p_tick(this, p):
        this.stack += 1
        print 'tick', p.now()
        if this.stack >= this.stackmax:
            this.tick.disable()
            this.charging = 0
        else:
            this.tick.timing += this.cd

def main():
    tl = Timeline()
    s = Skill(tl)
    s.cast()
    print s.tick.ctx.timeline
    
    tl.run(100)


if __name__ == "__main__":
    main()
