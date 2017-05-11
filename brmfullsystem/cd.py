from event import *

class cd(object):
    _enable = 1
    _last = 0
    _cooldown = 10
    el = 0
    _cdev = 0
    class CdEv(Event):
        def process(this):
            this.src._enable=1

    def __init__(this,eventlist):
        this._enable = 1
        this.el = eventlist
        this._cdev = cd.CdEv()
        this._cdev.src = this

    def enable(this):
        if this._enable == False or this._enable == None:
            return False
        if this._enable != 0:
            return True
        return False

    def cast(this):
        this._enable = 0
        this._cdev.time = this.el.time + this._cooldown
        this._cdev.addto(this.el)

    def last(this):
        return this._last


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
    a = cd(el)
    print a
    b = PrintEv(a)
    b.addto(el)
    a.cast()
    print 'a._enable',a._enable
    print 'a.enable()',a.enable()
    print 'b.a.enable()',b.a.enable()
    el.run(15)


if __name__ == '__main__' :
    main()


