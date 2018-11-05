from timeline import *


class Spells(object):
    pass


class Auras(object):
    pass

class Stats(object):
    class buff(object):
        prior = 0
        value = 0

    def add(this,stat):
        return stat + this.value
    def mult(this,stat):
        return stat * this.value

    def __init__(this):
        effect = this.add
        c = 0.1
        h = 0.0
        m = 0.8
        v = 0.0
        _c = 0.1
        _h = 0.0
        _m = 8
        _v = 0.0

    def refresh(this):
        c = _c
        h = _h
        m = _m
        v = _m

        
    def __setattr__(this, name, value):
        object.__setattr__(this, name, value)
    def __getattr__(this, name, value):
        object.__getattr__(this, name, value)

class Classes(object):
    def __init__(this):
        #this.tl = Timeline

        this.stats = Stats()
        this.spells = Spells()
        this.auras = Auras()

        this.gcd = Repeat_event(proc=this.p_gcd, interval=1)
        this.gcd.idle = 0

        this.foo = this.Foo()


    class Foo(object):
        cding = 0
        def __init__(this):
            this.foocd = Event("foocd",this.p_foocd)
            this.foocd.off()

        def cast(this):
            print '-- foo!', now()
            this.cding = 1
            this.foocd.enable(now()+6.5)

        def p_foocd(this, e):
            print '-- p_foocd'
            this.cding = 0
            e.disable()


    def p_gcd(this, e):
        if this.act_gcd() :
            e.idle = 0
            e.interval = 1
        else:
            e.idle = 0
            e.interval = 0.1

    def act_gcd(this):
        print 'gcd @', now()
        if not this.foo.cding :
            this.foo.cast()
            return 1
        else:
            #print '!foo', now()
            return 0


    def run(this):
        this.gcd.enable()
        this.ctx.run(20)

def main():
    import time
    time1 = time.time()
    c = Classes()
    c.run()
    time2 = time.time()
    #print time2-time1


if __name__ == "__main__":
    main()
