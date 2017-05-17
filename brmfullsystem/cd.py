from event import *

class cd(object):
    _enable = 1
    _cooldown = 10
    host = 0
    el = 0
    _cdev = 0
    withhaste = 0


    class CdEv(Event):
        def process(this):
            this.src._enable=1
            this.src.callback()

    def __init__(this,host,cooldown,withhaste=0):
        this._enable = 1
        this._cooldown = cooldown
        this.host = host
        this.el = host.el
        this.withhaste = withhaste
        this._cdev = cd.CdEv()
        this._cdev.src = this
        this._cdev.withhaste = this.withhaste

    def enable(this):
        if this._enable == False or this._enable == None:
            return False
        if this._enable != 0:
            return True
        return False

    def callback(this):
        #print '===========\n=========\n===========',this.el.time
        pass

    def cast(this):
        if this._enable != 0 :
            this._enable = 0
            this._cdev.time = this.el.time + this._cooldown
            this._cdev.addto(this.el)
            return 1
        else :
            return 0

    def last(this):
        return this._cdev.time - this.el.time


class stack(object):
    _stack = 0
    _stackmax = 0
    _cooldown = 10
    host = 0
    el = 0
    _cdev = 0


    class CdEv(RepeatEvent):
        def process(this):
            this.src._stack += 1
            if this.src._stack >= this.src._stackmax :
                this.repeat = 0
            this.callback()


    def __init__(this,host):
        this._enable = 1
        this.host = host
        this.el = host.el
        this._cdev = stack.CdEv()
        this._cdev.src = this

    def enable(this):
        if this._enable == False or this._enable == None:
            return False
        if this._enable != 0:
            return True
        return False

    def callback(this):
        pass

    def cast(this):
        if this._enable != 0 :
            this._enable = 0
            this._cdev.time = this.el.time + this._cooldown
            this._cdev.addto(this.el)
            return 1
        else :
            return 0

    def last(this):
        return this._cdev.time - this.el.time



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


