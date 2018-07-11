def now():
    return Context.activeContext[0].now

class Context(object):
    activeContext = [0]
    timeline = 0

    @classmethod
    def setup(cls):
        cls.activeContext[0] = object.__new__(cls)


    @classmethod
    def reset(cls):
        cls.activeContext[0] = 0
        return Context()


    def __new__(cls):
        if not cls.activeContext[0] :
            cls.activeContext[0] = object.__new__(cls)
        return cls.activeContext[0]

    def __init__(this):
        if not this.timeline:
            this.timeline = 1
            this.timeline = Timeline()
        this.now = 0


    def run(this,*args, **argv):
        this.timeline.run(*args, **argv)


class Event(object):
    #class Context(object):
    #    timeline = 0
    #ctx = Context()
    #@classmethod
    #def setup(cls,timeline):
    #    cls.ctx.timeline = timeline
    #    return cls.ctx
    #@classmethod
    #def reset(cls,timeline=None):
    #    cls.ctx = Event.Context()
    #    if timeline:
    #        cls.ctx.timeline = timeline
    #    return cls.ctx

    def __init__(this, proc=None, timing=0, ctx=None):
        if proc:
            this.process = proc
        else:
            this.process = this._process

        if not ctx:
            this.ctx = Context()
        else:
            this.ctx = ctx

        this.timing = timing

        this.online = 0

    
    def now(this):
        return this.ctx.now


    def disable(this):
        if this.online:
            this.online = 0
            this.ctx.timeline.rm(this)
    off = disable


    def enable(this, timing = None):
        if timing:
            this.timing = timing
        if this.online == 0:
            this.online = 1
            this.ctx.timeline.add(this)
    on = enable


    def callback(this):
        this.process(this)
        if this.timing <= this.now():
            if this.online:
                this.ctx.timeline.rm(this)


    @staticmethod
    def _process(timing):
        # sample plain _process
        print '-- plain event @', timing
        return 1


class RepeatEvent(Event):
    def __init__(this,proc=None,interval=10):
        super(RepeatEvent,this).__init__(proc)
        this.interval = interval

    def callback(this):
        this.process(this)
        if this.timing == this.now():
            this.timing += this.interval



class Timeline(object):

    def __init__(this, ctx=None):
        this._events = []
        if not ctx:
            this.ctx = Context()
        else:
            this.ctx = ctx


    def __str__(this):
        return "Timeline Events: %s"%(str(this._events))


    def now(this):
        return this.ctx.now


    def add(this, event):
        this._events.append(event)


    def rm(this, event):
        i = this._events.index(event)
        return this._events.pop(i)


    def process_head(this):
        eventcount = len(this._events)
        if eventcount == 0:
            return -1

        headtiming = this._events[0].timing
        headindex = 0

        if eventcount >= 2:
            for i in range(1,eventcount):
                timing = this._events[i].timing
                if timing < headtiming:
                    headtiming = timing
                    headindex = i
        if headtiming >= this.now():
            this.ctx.now = headtiming
            this._events[headindex].callback()
        else:
            print "timeline time err"
            exit()
            this._events.pop(headindex)
        return 0
    

    def run(this, last = 100):
        while 1:
            if this.now() > last:
                return
            r = this.process_head()
            if r == -1:
                return


def main():

    def a1(e):
        print 'a1', e.timing
        e.timing += 2
    def a2(e):
        print 'a2', e.timing

    ctx = Context()

    e1 = Event()
    e1.timing = 2
    e1.process = a1
    e1.on()

    ctx2 = Context.reset()
    #Event.setup(t2)
    e2 = RepeatEvent()
    e2.timing = 1.5
    e2.process = a2
    e2.on()

    e3 = Event()
    e3.timing = 2
    e3.process = a1
    e3.on()

    ctx.timeline.run(10)
    ctx2.timeline.run(30)


if __name__ == '__main__' :
    main()
