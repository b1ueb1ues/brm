class Processor(object):
    def __init__(this, cb=0, timing=0, interval=0):
        this.handler = -1
        this.timeline = Timeline()
        this.set(timing, interval, cb)


    def set(this, timing=0, interval=0, cb=0):
        this.timing = int(timing * 1000)
        this.interval = int(interval * 1000)

        if not timing :
            if not interval :
                this.interval = 1
            if this.interval > 1:
                this.timing = this.timeline._now

        if cb:
            this.register(cb)
        else:
            this.register(this._process)


    def now(this):
        if this.timeline:
            return this.timeline.now()


    def enable(this):
        if this.interval > 1:
            this.timing = this.timeline._now
        this.timeline.add(this)
        return this


    def disable(this):
        this.timeline.rm(this)
        return this
    
    def move(this, tl):
        tl.mv(this)


    def register(this, cb):
        this._process = cb
        if not this.timing and this.interval==1:
            this.process = this._direct
        else:
            this.process = this._check


    def _check(this, timing):
        if this.interval : # repeat
            if (timing - this.timing) % this.interval == 0:
                this._process(this)
        else : # proc once
            if (timing - this.timing) == 0:
                this._process(this)
                this.disable()


    def _direct(this, timing):
        this._process(this)


    @staticmethod
    def _process(timing):
        # sample plain _process
        if not this.timing :
            print '-- plain tick processor @', timing
        elif this.interval :
            print '-- plain interval processor per %d @ %d'%(this.interval, timing)
        else :
            print '-- plain once processor @', timing


    def process(): # virtual
        "this is the main process for outer to call"
        "but it is actually no need to def hear"
        "just for reference"

#{{{
    def _disable(this):
        def nop(timing):
            return
        this.process = nop

    def _enable(this):
        if this.timing :
            this.process = this._check
        else:
            this.process = this._process
#}}}
#} class Processor


class Timeline(object):
    'timeline for every 0.001s'
    def __init__(this):
        this._now = 0
        this.nextid = 0
        this.processors = {}
        #this.disabled = {}
        this.p2add = []
        this.h2rm = []
        pass

    def run(this, time=10, interval = 0.001):
        _interval = int(interval * 1000)
        _time = int(time * 1000)
        i = 0 - _interval
        while 1:
            i += _interval
            if i >= _time:
                break
            this._now = i
            #this.now += 1
            this._process(i)


    def createp(this, cb, timing=0, interval=0):
        p = Processor(cb,timing,interval)
        p.timeline = this
        handler = this.nextid
        this.nextid += 1
        p.handler = handler 
        return p


    def now(this):
        return this._now / 1000.0


    def add(this, p):
        this.p2add.append(p)
        return handler

    def rm(this, p):
        this.h2rm.append(p.handler)

    def mv(this, p):
        p.timeline = this
        handler = this.nextid
        this.nextid += 1
        p.handler = handler 

    def _async_add(this):
        for i in this.p2add:
            this.processors[i.handler] = i
        this.p2add = []


    def _async_rm(this):
        for i in this.h2rm:
            this.processors.pop(i)
        this.h2rm = []


    def _process(this, timing):
        this._async_rm()
        this._async_add()
        for i in this.processors:
            p = this.processors[i]
            p.process(timing)

class test(object):
    def __init__(this):
        this.p = Processor()
        this.p.register(this.foo)
    def foo(this, proc):
        print '++ class tick processor @', proc.now(), proc.timing, proc.interval


def main():
    def b(p):
        print '-- modified interval processor @', p.now(), p.timing, p.interval
        if p.now() >= 0.05:
            p.disable()
    def c(p):
        print '-- modified once processor @', p.now(), p.timing, p.interval
        p.pp.enable()

    t = Timeline()

    ob = test()

    pp = t.createp(b, 0.01,0.01)
    po = t.createp(c, 0.07,0)
    po.pp = pp

    t.add(ob.p)
    #t.add(pp)
    #t.add(po)
    t.run(0.1)

if __name__ == "__main__" :
    main()
