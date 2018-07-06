class Event(object):
    class Context(object):
        timeline = 0
    ctx = Context()

    def __init__(this, timeline=None, proc=None):
        if timeline:
            this.ctx.timeline = timeline
        if proc:
            this.process = proc
        else:
            this.process = this._process

        this.timing = 0
        this.online = 0
    
    def now(this):
        return this.ctx.timeline.now()

    def disable(this):
        if this.online:
            this.online = 0
            this.ctx.timeline.rm(this)
    off = disable

    def enable(this, timing = None):
        if this.online == 0:
            this.online = 1
            this.ctx.timeline.add(this, timing)
    on = enable

    def callback(this):
        this.process(this)
        if this.timing == this.now():
            if this.online:
                this.ctx.timeline.rm(this)

    @staticmethod
    def _process(timing):
        # sample plain _process
        print '-- plain event @', timing
        return 1

class RepeatEvent(Event):
    def __init__(this):
        this.repeat = 10

    def callback(this):
        this.process(this)
        if this.timing == this.now():
            this.timing += this.repeat



class Timeline(object):
    class Context(object):
        nextid = 0
    ctx = Context()

    def __init__(this):
        this._events = []
        this._now = 0

    def __str__(this):
        return str(this._events)

    def now(this):
        return this._now

    def add(this, event, timing = None):
        event.ctx.timeline = this
        if timing != None:
            event.timing = timing
        this._events.append(event)

    def rm(this, event):
        i = this._events.index(event)
        return this._events.pop(i)

    def newevent(this, proc) :
        return Event(this, proc)
        
    
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
        if headtiming >= this._now:
            this._now = headtiming
            this._events[headindex].callback()
        else:
            this._events.pop(headindex)
        return 0
    
    def run(this, last = 100):
        while 1:
            if this._now > last:
                return
            r = this.process_head()
            if r == -1:
                return


def main():
    t = Timeline()

    def a1(e):
        print 'a1', e.timing
    def a2(e):
        print 'a2', e.timing

    e1 = Event()
    e1.timing = 2
    e1.process = a1

    e2 = RepeatEvent()
    e2.timing = 1.5
    e2.process = a2


    t.add(e1)
    t.add(e2)

    print t
    t.run()


if __name__ == '__main__' :
    main()
