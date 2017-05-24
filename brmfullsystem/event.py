
class Event(object):
    time = 0
    dst = 0
    src = 0
    el = 0
    withhaste = 0

    def addto(this, el):
        el.add(this)

    def __init__(this,el=0, src = 0, time=0, dst = 0, withhaste = -2):
        this.time = time
        this.src = src
        this.dst = dst
        if withhaste != -2:
            this.withhaste = withhaste
        if el != 0:
            this.addto(el)
    def __repr__(this):
        return this.__class__.__name__+" at %.2f"%this.time
    def __str__(this):
        return this.__class__.__name__+" at %.2f"%this.time

    def now(this):
        return this.el.time

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
    def __init__(this,el = 0, src = 0, repeat = -2 ,time = 0.0, dst = 0, withhaste = -2):
        super(RepeatEvent,this).__init__(el, src, time, dst, withhaste)
        if repeat != -2 :
            this.repeat = repeat

    def repeatproc(this):
        print this.time,this,'repeatproc (deprecated)'
        exit()

    def elprocess(this):
        this.process()
        if this.repeat <= 0 :
            return
        if this.withhaste != 0:
            try:
                this.time += this.repeat / this.el._oldhaste
            except Exception,e:
                print this, this.time, this.el
                print '-this--',this
                print '-src--',this.src, this.src.stack()
                print '-el---',this.src.src.el
                print '-repeat----',this.repeat
                print '-now---',this.src.src.el.time
                print e
                exit()
        else:
            #print this.el._list
            if 'd' in str(this):
                print '!'
                exit()
            this.time += this.repeat
        this.el.add(this)

    def process(this):
        print this.time,'repeatev proc'


#}class repeatevent

class Eventlist(object):
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


    def add(this,event,time=-2):
        event.el = this
        if event.src == 0 :
            event.src = this.src
        if this.debug >= 2:
            print "%.2f"%this.time,'add',event
        if time != -2 :
            event.time = time
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
        print trackstack
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
        if this.debug != 0 :
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

class Eventlist_withhaste(Eventlist):
    _hastelist = []
    _oldhaste = 1
    def __init__(this,src=0,debug=0):
        super(Eventlist_withhaste,this).__init__(src,debug)
        _hastelist = []
        _oldhaste = 1
    #}__init__
    def add_withhaste(this,event,time=-2):
        if this.debug >= 1:
            print event.__dict__
        event.el = this
        if event.src == 0 :
            event.src = this.src
        if this.debug :
            print "%.2f"%this.time,'addhaste',event
        if time != -2 :
            event.time = time
        timing = event.time
        for i in range(len(this._hastelist)) :
            if timing <= this._hastelist[i].time  :
                tmp = this._hastelist[:i]
                tmp.append(event)
                tmp += this._hastelist[i:]
                this._hastelist = tmp
                return True
        this._hastelist.append(event)
    #}

    def add(this,event,time=-2):

        if event.withhaste != 0:
            this.add_withhaste(event,time)
            return
        else:
            this.add_withouthaste(event,time)
            return
    #}

    def add_withouthaste(this,event,time=-2):
        #print 'print awh'
        event.el = this
        if event.src == 0 :
            event.src = this.src
        if this.debug >= 2:
            print "%.2f"%this.time,'add',event
        if time != -2:
            event.time = time
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
    
    def synchaste(this):
        haste = this.src.gethaste()
        if haste == this._oldhaste:
            return
        change = haste / this._oldhaste
        for i in this._hastelist :
            tmp = i.time - this.time
            tmp = tmp/change + this.time
            i.time = tmp
        this._oldhaste = haste


    def processone(this):
        if this.debug != 0:
            print 'thistime!!!!!!!',this.time
            print 'in hasteprocessone'
            print this._list,'\n',this._hastelist,'\n'
        this.synchaste()
        iv1 = None
        iv2 = None
        if this._list != []:
            iv1 = this._list[0].time - this.time
        if this._hastelist != []:
            iv2 = this._hastelist[0].time - this.time

        if iv1 == None :  #and iv2 != 0
            if iv2 == None :
                if this.debug != 0:
                    print 'return',this._list,this._hastelist
                return 
            e = this._hastelist.pop(0)
        elif iv2 == None : #and iv1 != 0
            e = this._list.pop(0)
        elif iv1 < iv2:
            e = this._list.pop(0)
        else :
            e = this._hastelist.pop(0)


#        this.count += 1
#        print this._list

        if this.debug :
            print '>>>>>hasteprocone',e,'\n',this._list,'\n',this._hastelist,'\n'
        if this.time < e.time:
            this.time = e.time
        e.elprocess()
#        if this.count >=3:
#            exit()
        return #this.time

    def rm(this,event):
        if event.withhaste != 0 :
            _list = this._hastelist
        else :
            _list = this._list
        for i in range(len(_list)) :
            if _list[i] == event :
                ret = _list.pop(i)
                event.el = 0
                #print '--rm',this.time,event
                return ret
        print this.time, ': haste rm 404', event
        print this
        print trackstack
        exit()
        return 0


    def mv(this, event, offset = 0, time = 0):
        if offset != 0:
            e = this.rm(event)
            if e == 0 :
                print this.time,': move 404', event
                return 
            e.time += offset
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
#}class repeatlist



def main():
    class test(object):
        def gethaste(this):
            return 2

    a = test()

    el = Eventlist_withhaste(src=a,debug = 1)
    e1 = RepeatEvent(repeat = 3)
    e2 = RepeatEvent(repeat = 4,withhaste=1)
    e1.addto(el)
    e2.addto(el)
    el.run(20)




if __name__ == '__main__' :
    main()
