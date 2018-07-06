class Event(object):
    class Context(object):
        timeline = 0
    ctx = Context()

    def __init__(this):
        this.ctx.timeline = 0
        this.timing = 0
        this.process = this._process
    
    def now(this):
        return this.ctx.timeline.now

    def disable(this):
        this.ctx.timeline.rm(this)

    def callback(this):
        this.process(this)
        if this.timing == this.now():
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
        this.now = 0

    def __str__(this):
        return str(this._events)

    def add(this, event, timing = None):
        event.ctx.timeline = this
        if timing != None:
            event.timing = timing
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
        this.now = headtiming
        this._events[headindex].callback()
        return 0
    
    def run(this, last = 100):
        while 1:
            if this.now > last:
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
