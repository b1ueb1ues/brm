class Processor(object):
    def __init__(this, timing=0, period=0, func=0):
        this.timing = int(timing * 1000)
        this.period = int(period * 1000)
        if not timing and not period :
            this.period = 1

        if func:
            this.register(func)
        else:
            this.register(this._process)

    def register(this, func):
        this._process = func
        if this.timing :
            this.process = this._check
        else:
            this.process = this._direct

    def disable(this):
        def nop(timing):
            return
        this.process = nop

    def enable(this):
        if this.timing :
            this.process = this._check
        else:
            this.process = this._process


    def _check(this, timing):
        if this.period :
            if (timing - this.timing) % this.period == 0:
                this._process(this,timing)
        else :
            if (timing - this.timing) == 0:
                this._process(this,timing)

    def _direct(this, timing):
        this._process(timing)


    @staticmethod
    def _process(timing):
        # sample plain _process
        if not this.timing :
            print '-- plain tick processor @', timing
        elif this.period :
            print '-- plain period processor per %d @ %d'%(this.period, timing)
        else :
            print '-- plain once processor @', timing

    def process(): # virtual
        "this is the main process for outer to call"
        "but it is actually no need to def hear"
        "just for reference"


class Timeline(object):
    'timeline for every 0.001s'
    def __init__(this):
        this._now = 0
        this.nextid = 0
        this.processors = {}
        this.disabled = {}
        pass

    def run(this,time=10):
        _time = int(time * 1000)
        for i in range(_time):
            this.process()
            this._now += 1

    def add(this, p):
        handler = this.nextid
        this.nextid += 1
        this.processors[handler] = p
        return handler
    def rm(this, handler):
        this.processors.pop(handler)


    def process(this):
        for i in this.enabled:
            enabled[i].process(this._now)

class test(object):
    def __init__(this):
        this.p = Processor()
        this.p.register(this.foo)
    def foo(this, timing):
        print '++ class tick processor @', timing


def main():
    def b(this, timing):
        print '-- modified period processor @', timing, this.timing, this.period
        if timing >= 50:
            this.disable()
    def c(this, timing):
        print '-- modified once processor @', timing, this.timing, this.period
        this.pp.enable()

    ob = test()

    pp = Processor(0.01,0.01)
    pp.register(b) 
    po = Processor(0.07,0)
    po.register(c)
    po.pp = pp

    t = Timeline()
    t.processor.append(ob.p)
    t.processor.append(pp)
    t.processor.append(po)
    t.run(0.1)

if __name__ == "__main__" :
    main()
