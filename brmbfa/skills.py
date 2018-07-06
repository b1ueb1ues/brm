from timeline import Timeline
import time

class Skill(object):
    def __init__(this, tl, src=0, dst=0):
        this.tl = tl
        this.cd = 8
        this.stackmax = 3
        this.stack = this.stackmax

        this.charge = 0
        this.tick = this.tl.createp(this.p_tick)

        this.charging = 0


    def haste(this):
        return 0

    def cast(this):
        if this.stack >= 1:
            this.stack -= 1
            if not this.charging :
                this.charging = 1
                this.tick.enable()
            return 0
        else:
            return this.cd - this.charge

    def p_tick(this, p):
        h = 1.0 + this.haste()
        this.charge += 0.001 * h 
        if this.charge >= this.cd :
            this.charge -= this.cd
            this.stack += 1
            if this.stack >= this.stackmax:
                this.tick.disable()
                this.charging = 0

def main():
    tl = Timeline()
    s = Skill(tl)
    s.cast()
    s.cast()
    s.cast()
    time1 = time.ctime()
    tl.run(100)
    time2 = time.ctime()
    print time1, time2


if __name__ == "__main__":
    main()
