if __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from timeline import *
import time

class Spell(object):
    config = {
        "cd":8,
        "stackmax":3,
        "hashaste":0,
        "_END":0
    }
    effects = []

    def __init__(this, src=0, dst=0):
        this.ctx = Context()
        this.src = src
        this.dst = dst
        this._haste = 1

        this.cdstart = None

        this.init()

        for i in this.config:
            this.__setattr__(i,this.config[i])

        this.stack = this.stackmax
        this.cdtick = Event(this.p_cdtick)

    def init(this):
        pass


    def sethaste(this):
        return 0


    def cast(this):
        print this, this.stack,this.stackmax
        if this.stack >= 1:
            this.stack -= 1
            if this.cdstart == None:
                this.cdstart = now()
                this.cdtick.enable(now() + this.cd/this._haste)
                this.effect()
            return 0
        else:
            print this.cd, now(), this.cdstart
            return this.cd - (now() - this.cdstart)

    def reduce(this,time):
        n = now()
        this.cdtick.timing -= time
        if this.cdtick.timing < n:
            this.cdtick.timing = n


    def effect(this):
        pass

    def p_cdtick(this, p):
        this.stack += 1
        this.cdstart = now()
        print 'cdtick', p.now()
        if this.stack >= this.stackmax:
            this.cdtick.disable()
            this.cdstart = None
        else:
            this.cdtick.timing += this.cd

def main():
    c = Context()
    s = Spell()

    def test(e):
        print '@',now(),':',
        print 'cast',e.s.cast(),
        print 'cast',e.s.cast(),
        print 'cast',e.s.cast(),
        print 'cast',e.s.cast()
    e = Event(test)
    e.s = s
    e.enable(10)


    s.cast()
    s.cast()
    print c.timeline
    
    c.run(100)


if __name__ == "__main__":
    main()
