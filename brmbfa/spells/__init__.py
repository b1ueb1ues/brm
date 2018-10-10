if __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from timeline import *
import time

class Spell(object):
    config = {}
    config_init = {
        "spellname": "null" ,
        "_cd"       : 1  ,
        "_stack_max" : 1  ,
        "_has_haste" : 0  ,
        "_cost"     : {} ,
        "_channel"  : 0  ,
        "_cast"     : 0  ,
        "_END"     : 0
    }
    effects = []

    def __init__(this, src=0, dst=0):
        this.src = src
        this.dst = dst
        this._haste = 1

        this.cdstart = None

        this.init()

        for i in this.config_init:
            this.__setattr__(i,this.config_init[i])
        for i in this.config:
            this.__setattr__(i,this.config[i])

        this._stack = this._stack_max
        this.cdtick = Event('cdtick',this.p_cdtick)
        this.cdtick.off()

    def init(this):
        pass


    def set_haste(this):
        return 0

    def check(this):
        if this._stack <= 0 :
            return 'nostack', this.cdtick.timing - now()
        if this._cost != {}:
            return this.src.cost(this._cost)
        Event(this.__class__)
        return 'noerr'


    def cast(this):
        print this, this._stack,this._stack_max
        if this._stack >= 1:
           # if this.src.cost() < 0:
           #     return 

            this._stack -= 1
            if this.cdstart == None:
                this.cdstart = now()
                this.cdtick.enable(now() + this._cd/this._haste)
                this.effect()
            return 0
        else:
            print this._cd, now(), this.cdstart
            return this._cd - (now() - this.cdstart)

    def reduce(this,time):
        n = now()
        this.cdtick.timing -= time
        if this.cdtick.timing < n:
            this.cdtick.timing = n


    def effect(this):
        pass

    def p_cdtick(this, p):
        this._stack += 1
        print 'cdtick', now()
        if this._stack >= this._stack_max:
            this.cdtick.disable()
            this.cdstart = None
        else:
            this.cdstart = now()
            this.cdtick.timing += this._cd

def main():
    s = Spell()

    def test(e):
        print '@%d'%now(),':',
        print 'cast',e.s.cast(),
        print 'cast',e.s.cast(),
        print 'cast',e.s.cast(),
        print 'cast',e.s.cast()
    e = Event('test',test)
    e.s = s
    e.enable(10)

    s.cast()
    s.cast()
    print Timeline()
    print 'run---------'
    Timeline().run()
    


if __name__ == "__main__":
    main()
