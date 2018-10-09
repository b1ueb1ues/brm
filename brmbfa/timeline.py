
class Event(object):

    def __init__(this, name, proc=None, timing=None, timeline=None):
        this.name = name

        if proc:
            this.process = proc
        else:
            this.process = this._process

        if timeline:
            this.timeline = timeline
        else:
            this.timeline = Timeline()

        if timing :
            this.timing = timing
        else:
            this.timing = now()

        this._trigger = []
        this.online = 0
        this.on()

    def disable(this):
        if this.online:
            this.online = 0
            this.timeline.rm(this)
    #alias
    off = disable


    def enable(this, timing = None):
        if timing:
            this.timing = timing
        if this.online == 0:
            this.online = 1
            this.timeline.add(this)
    #alias
    on = enable


    def callback(this):
        this.process(this)
        for i in this._trigger:
            i()
        if this.timing <= now():
            if this.online:
                this.timeline.rm(this)


    def process(this):
        pass
    @staticmethod
    def _process(timing):
        # sample plain _process
        print '-- plain event @', timing
        return 1


class RepeatEvent(Event):
    def __init__(this, name, proc=None, interval=10):
        super(RepeatEvent,this).__init__(name, proc)
        this.interval = interval

    def callback(this):
        this.process(this)
        if this.timing == now():
            this.timing += this.interval




__g_now = 0

def now():
    global __g_now
    return __g_now
def set_time(time):
    global __g_now
    __g_now = time
    return 1

__g_event_listener_mismatch = {} # {"name":[]}
__g_trigger_onload = {}

def add_event_listener(eventname,listener):
    global __g_eventlistener 
    global __g_trigger_onload

    if eventname in __g_trigger_onload:
        __g_trigger_onload[eventname].append(listener)
    elif eventname in __g_eventlistener_mismatch :
        __g_eventlistener_mismatch[eventname].append(listener)
    else:
        __g_eventlistener_mismatch[eventname] = listener

def add_event_trigger(eventname, trigger):
    global __g_eventlistener 
    global __g_trigger_onload

    __g_trigger_onload[eventname] = trigger



class Timeline(object):
    _active = [0]
    _now = 0
    _listenerlist = []
    _eventlist = []

    @classmethod
    def setup(cls):
        cls.activeContext[0] = object.__new__(cls)


    @classmethod
    def reset(cls):
        cls._active = [0]
        return Timeline()

    def __init__(this):
        if this._active[0]:
            return
        this._listenerlist = []
        this._eventlist = []

    def __new__(cls):
        if not cls._active[0] :
            cls._active[0] = object.__new__(cls)
        return cls._active[0]


    def __str__(this):
        return "Timeline Eventlist: %s"%(str(this._eventlist))


    def add(this, event):
        this._eventlist.append(event)


    def addlistener(this, listener):
        this._listenerlist.append(listener)


    def rm(this, event):
        i = this._eventlist.index(event)
        return this._eventlist.pop(i)


    def process_head(this):
        global __g_now
        eventcount = len(this._eventlist)
        if eventcount == 0:
            return -1

        if eventcount == 1:
            headtiming = this._eventlist[0].timing  
            headindex = 0                          
        else: #if eventcount >= 2: 
            headtiming = this._eventlist[0].timing  
            headindex = 0                          
            for i in range(1,eventcount):
                timing = this._eventlist[i].timing
                if timing < headtiming:
                    headtiming = timing
                    headindex = i

        if headtiming >= now():
            set_time(headtiming)
            headevent = this._eventlist[headindex]
            headevent.callback()
            for i in this._listenerlist:
                i(headevent)
        else:
            print "timeline time err"
            exit()
        return 0
    
    @classmethod
    def run(cls, last = 100):
        while 1:
            if now() > last:
                return
            r = cls.process_head(cls._active[0])
            if r == -1:
                return


def main():

    def a1(e):
        print e.name, e.timing
        e.timing += 2
    def a2(e):
        print e.name, e.timing
    def a3(e):
        print e.name, e.timing

    class Test():
        def __init__(this):
            this.e = Event("test",this.processb,5).on()
            print Timeline()

        def processb(this, e):
            print e.name, e.timing

    e1 = Event("e1",a1,2)
    e2 = RepeatEvent("e2",a2,1.5)
    e3 = Event("e3",a3,3)
    Test()
    e1.process = a1
    e2.process = a2
    e3.process = a3

    Timeline().run()



if __name__ == '__main__' :
    main()
