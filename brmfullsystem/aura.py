from event import *

class aura(object):
    _enable = 0
    duration = 10
    src = 0
    el = 0
    _auraev = 0
    withhaste = 0
    casttime = 0



    class AuraEv(Event):
        def process(this):
            this.src._enable=0
            this.src.endprocess(this.el.time)

    def __init__(this,src,duration=-2,withhaste=-2,el=0):
        this._enable = 0
        if duration != -2:
            this.duration = duration
        if withhaste != -2:
            this.withhaste = withhaste
        this.src = src
        if el != 0:
            this.el = el
        else:
            this.el = src.el
        this._auraev = aura.AuraEv()
        this._auraev.src = this
        this._auraev.withhaste = this.withhaste

    def enable(this):
        if this._enable == False or this._enable == None:
            return 0
        if this._enable != 0:
            return 1
        return 0

    def endprocess(this,time):
        pass
    def startprocess(this,time):
        pass
    def refreshprocess(this,time):
        this._auraev.mv(time=this.el.time+this.duration)

    def cast(this):
        this.casttime = this.el.time
        if this._enable == 0 :
            this._enable = 1
            if this.withhaste != 0:
                this._auraev.time = this.el.time + this.duration/this.el._oldhaste
            else:
                this._auraev.time = this.el.time + this.duration
            this._auraev.addto(this.el)
            this.startprocess(this.el.time)
            return 1
        else :
            this.refreshprocess(this.el.time)
            return 2

    def reduce(this,offset=1):
        this._auraev.mv(offset = 0.0-offset)

    def delay(this,offset=1):
        this._auraev.mv(offset = offset)

    def now(this):
        return this.el.time


    def last(this):
        return this._auraev.time - this.el.time

    def time(this):
        return this._auraev.time

class PrintEv(RepeatEvent):
    repeat = 1
    def __init__(this,a):
        this.a = a
        print 'print init',this.a
        print 'print init a.enable()',this.a.enable(),this.a._enable
    def process(this):
        print this.time,this.a.enable(),this.a._enable

def main():
    el = Eventlist()
    a = aura(src=0,el=el)
    print a
    b = PrintEv(a)
    b.addto(el)
    a.cast()
    print 'a._enable',a._enable
    print 'a.enable()',a.enable()
    print 'b.a.enable()',b.a.enable()
    el.run(5)
    a.cast()
    el.run(20)


if __name__ == '__main__' :
    main()


