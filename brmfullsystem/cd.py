from event import *

class cd(object):
    _enable = 1
    _cooldown = 10
    src = 0
    el = 0
    _cdev = 0
    withhaste = 0
    casttime = 0


    class CdEv(Event):
        def process(this):
            this.src._enable=1
            this.src.endprocess(this.el.time)

    def __init__(this,src,cooldown=-2,withhaste=-2):
        this._enable = 1
        if cooldown != -2:
            this._cooldown = cooldown
        if withhaste != -2:
            this.withhaste = withhaste
        this.src = src
        this.el = src.el
        this._cdev = cd.CdEv()
        this._cdev.src = this
        this._cdev.withhaste = this.withhaste

    def enable(this):
        if this._enable == False or this._enable == None:
            return False
        if this._enable != 0:
            return True
        return False

    def endprocess(this,time):
        #print '===========\n=========\n===========',this.el.time
        pass
    def startprocess(this,time):
        pass

    def cast(this):
        if this._enable != 0 :
            this.casttime = this.el.time
            this._enable = 0
            this._cdev.time = this.el.time + this._cooldown
            this._cdev.addto(this.el)
            return 1
        else :
            return 0

    def reduce(this,offset=1):
        this._cdev.mv(offset = 0.0-offset)


    def last(this):
        return this._cdev.time - this.el.time

    def time(this):
        return this._cdev.time


class stack(object):
    _stack = 0
    _stackmax = 0
    _cooldown = 10
    src = 0
    el = 0
    _cdev = 0
    withhaste = 0


    class CdEv(RepeatEvent):
        def process(this):
            this.src._stack += 1
            if this.src._stack >= this.src._stackmax :
                this.repeat = 0
                this.src.endprocess(this.el.time)
            else:
                this.src.stackprocess(this.el.time)


    def __init__(this,src,cooldown=-2,withhaste=-2):
        if cooldown != -2:
            this._cooldown = cooldown
        if withhaste != -2:
            this.withhaste = withhaste

        this.src = src
        this.el = src.el

        this._cdev = stack.CdEv()
        this._cdev.src = this
        this._cdev.withhaste = this.withhaste
        this._cdev.time = this.el.time + this._cooldown
        this._cdev.repeat = this._cooldown
        if this._stack < this._stackmax :
            this._cdev.addto(this.el)

    def enable(this):
        if this._stack >= 1 :
            return True
        return False

    def stack(this):
        return (this._stack,this._stackmax)

    def startprocess(this,time):
        pass
    def endprocess(this,time):
        pass
    def stackprocess(this,time):
        pass

    def cast(this):
        #print 'cast',this.src.el.time
        if this._stack >= this._stackmax :
            this._stack -= 1
            this._cdev.time = this.el.time + this._cooldown
            this._cdev.repeat = this._cooldown
            this._cdev.addto(this.el)
            this.startprocess(this.el.time)
            return 1
        elif this._stack >= 1 :
            this._stack -= 1
            this.startprocess(this.el.time)
            return 1
        else:
            return 0

    def reduce(this,offset=1):
        if this._stack >= this._stackmax:
            print 'max'
            return 
        this._cdev.mv(offset= 0.0-offset)


    def time(this):
        return this._cdev.time

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


