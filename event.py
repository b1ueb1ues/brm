
class Event:
    time = 0
    dst = 0
    src = 0
    el = 0

    def addto(this, el):
        el.add(this)

    def __init__(this,el=0, src = 0, time=0, dst = 0):
        this.time = time
        this.src = src
        this.dst = dst
        if el != 0:
            this.addto(el)
    def __repr__(this):
        return this.__class__.__name__+" at %.2f"%this.time
    def __str__(this):
        return this.__class__.__name__+" at %.2f"%this.time

    def mv(this, offset = 0, time = 0):
        this.el.mv(this, offset, time)

    def rm(this):
        this.el.rm(this)

    def elprocess(this):
        this.process()

    def process(this):
        print this.time,'process'
#}

class RepeatEvent(Event):
    repeat = 1
    def __init__(this,el=0, repeat = -2 ,time=0.0, dst=0):
        Event.__init__(this,el, time, dst)
        if repeat != -2 :
            this.repeat = repeat

    def repeatproc(this):
        print this.time,this,'repeatproc (deprecated)'
        exit()

    def elprocess(this):
        this.process()
        if this.repeat <= 0 :
            return
        this.time += this.repeat
        this.el.add(this)

    def process(this):
        print this.time,'repeatev proc'


#}class repeatevent



class Eventlist:
    time = 0
    _list = []
    src = 0
    debug = 0
    def __str__(this):
        return str(this._list)

    def __init__(this,src=0,debug=0):
        this.src = src
        this._list = []
        this.debug = debug


    def add(this,event):
        event.el = this
        event.src = this.src
        if this.debug :
            print "%.2f"%this.time,'add',event
        timing = event.time
        for i in range(len(this._list)) :
            if timing <= this._list[i].time  :
                tmp = this._list[:i]
                tmp.append(event)
                tmp += this._list[i:]
                this._list = tmp
                return True
        this._list.append(event)
    #}
    
    def rm(this,event):
        for i in range(len(this._list)) :
            if this._list[i] == event :
                ret = this._list.pop(i)
                event.el = 0
                return ret
        print this.time, ': rm 404', event
        print this
        exit()
        return 0


    def mv(this, event, offset = 0, time = 0):
        if offset != 0:
            e = this.rm(event)
            if e == 0 :
                print this.time,': move 404', event
                return 
            e.time += offset
           # if e.time < this.time :
           #     e.time = this.time
            this.add(e)
        else :
           # if newtiming < this.time :
           #     newtiming = this.time
            e = this.rm(event)
            if e == 0 :
                print this.time,': move 404', event
                return 
            e.time = time
            this.add(e)


    count = 0
    def processone(this):
        e = this._list.pop(0)


#        this.count += 1
#        print this._list

        if this.debug :
            print e,this._list
        if this.time < e.time:
            this.time = e.time
        if this.debug :
            print '%.1f: '%this.time,e,this
        e.elprocess()
#        if this.count >=3:
#            exit()
        return #this.time
    

    def run(this, time = 9999):
        while(1):
            if this.time > time :
                return
            this.processone()

#} class eventlist

