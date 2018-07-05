class Processor(object):
    def __init__(this, cb=0, timing=0, interval=0):
        this.handler = -1
        this.timeline = Timeline()
        if not cb:
            cb = this._process
        this.set(timing, interval, cb)


    def set(this, timing=0, interval=0, cb=0):
        this.timing = int(timing * 1000)
        this.interval = int(interval * 1000)

        if not timing :
            #if not interval :
            #    this.interval = 1
            if not this.interval > 1:
                this.timing = this.timeline._now

        if cb:
            this._process = cb
            if not this.timing and not this.interval:
                this.process = this._direct
            else:
                this.process = this._check
       # if cb:
       #     this._register(cb)
       # else:
       #     this._register(this._process)


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
   # def settl(this, tl):
   #     tl.mv(this)


   # def _register(this, cb):
   #     this._process = cb
   #     if not this.timing and this.interval==1:
   #         this.process = this._direct
   #     else:
   #         this.process = this._check

#}}}

#} class Processor


class Timeline(object):
    'timeline for every 0.001s'
    s_nextid = [0]
    def __init__(this):
        this._now = 0
        this.processors = {}
        this.p2add = []
        this.h2rm = []
        pass

    def getnextid(this):
        return this.s_nextid[0]

    def newid(this):
        this.s_nextid[0] += 1
        return this.s_nextid[0] - 1

    def setnextid(this, n):
        this.s_nextid[0] = n
        

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
        handler = this.newid()
        p.handler = handler 
        return p


    def now(this):
        return this._now / 1000.0


    def add(this, p):
        this.p2add.append(p)
        #return handler

    def rm(this, p):
        this.h2rm.append(p.handler)

    def register(this, p):
        p.timeline = this
        handler = this.newid()
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


def main():
    def a(this, p):
        print 'a', p.now()
    def b(this, p):
        print 'b', p.now()
    def c(this, p):
        print 'c', p.now()

    t1 = Timeline()
    p1 = t1.createp(a, 0.01, 0.01)

    t2 = Timeline()
    p2 = t2.createp(b, 0.03, 0.01)
    p3 = t2.createp(c)

    print p1.handler
    print p2.handler
    print p3.handler
    

if __name__ == "__main__" :
    main()
