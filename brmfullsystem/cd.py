from event import *
count = 0

class cd(object):
    _enable = 1
    cooldown = 10
    src = 0
    el = 0
    _cdev = 0
    withhaste = 0
    casttime = 0


    class CdEv(Event):
        def process(this):
            this.src._enable=1
            if this.src._cdev == 0 :
                print '====',this.now(),this.src,this.src.casttime

            tmpev = cd.callbackev()
            tmpev.src = this.src
            tmpev.time = this.src.el.time
            tmpev.addto(this.src.el)

            this.src._cdev = 0

    class callbackev(Event):
        def process(this):
            this.src.endprocess(this.time)

    def __init__(this,src,cooldown=-2,withhaste=-2):
        this._enable = 1
        if cooldown != -2:
            this.cooldown = cooldown
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

            if this._cdev == 0:
                this._cdev = cd.CdEv()
                this._cdev.src = this
                this._cdev.withhaste = this.withhaste

            if this.withhaste != 0:
                this._cdev.time = this.el.time + this.cooldown/this.el._oldhaste
            else:
                this._cdev.time = this.el.time + this.cooldown
            this._cdev.addto(this.el)
            return 1
        else :
            return 0

    def reduce(this,offset=1):
        if this._cdev == 0 :
            return 0
        this._cdev.mv(offset = 0.0-offset)
        return 1

    def haste(this):
        return this.el._oldhaste

    def last(this):
        if this._cdev != 0:
            return this._cdev.time - this.el.time
        return 0

    def time(this):
        if this._cdev != 0:
            return this._cdev.time
        else:
            return -1

    def now(this):
        return this.el.time



class stack(object):
    _stack = 0
    _stackmax = 0
    cooldown = 10
    src = 0
    el = 0
    _cdev = 0
    withhaste = 0


    class stackcallbackev(Event):
        def process(this):
            this.src.stackprocess(this.time)

    class CdEv(RepeatEvent):
        def process(this):
            this.src._stack += 1
            if this.src._stack > this.src._stackmax:
                this.src._stack = this.src._stackmax
            if this.src._stack == this.src._stackmax :
                this.repeat = 0

                tmpev = stack.stackcallbackev()
                tmpev.src = this.src
                tmpev.time = this.src.el.time
                tmpev.addto(this.src.el)

                tmpev = cd.callbackev()
                tmpev.src = this.src
                tmpev.time = this.src.el.time
                tmpev.addto(this.src.el)

                this.src._cdev = 0
            else:
                tmpev = stack.stackcallbackev()
                tmpev.src = this.src
                tmpev.time = this.src.el.time
                tmpev.addto(this.src.el)
    

    def __init__(this,src,cooldown=-2,withhaste=-2):
        if cooldown != -2:
            this.cooldown = cooldown
        if withhaste != -2:
            this.withhaste = withhaste

        this.src = src
        this.el = src.el

        if this._stack < this._stackmax :
            this._cdev = stack.CdEv()
            this._cdev.src = this
            this._cdev.withhaste = this.withhaste
            this._cdev.repeat = this.cooldown
            if this.withhaste != 0 :
                this._cdev.time = this.el.time + float(this.cooldown)/this.haste()
            else:
                this._cdev.time = this.el.time + this.cooldown
            this._cdev.addto(this.el)

    def enable(this):
        if this._stack >= 1 :
            return True
        return False

    def stack(this):
        return (this._stack,this._stackmax)
    def setstack(this,stack,stackmax):
        this._stack = stack
        this._stackmax = stackmax


    def startprocess(this,time):
        pass
    def endprocess(this,time):
        pass
    def stackprocess(this,time):
        pass

    def cast(this):
        if this._stack >= this._stackmax :
            this._stack -= 1
            if this._cdev != 0 :
                return
            this._cdev = stack.CdEv()
            this._cdev.src = this
            this._cdev.withhaste = this.withhaste
            if this.withhaste != 0 :
                this._cdev.time = this.now() + this.cooldown/this.haste()
            else:
                this._cdev.time = this.now() + this.cooldown
            this._cdev.repeat = this.cooldown
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
            #print 'max'
            return 0
        #print this.now(),this._stack,this._stackmax,this._cdev
        if this._cdev != 0:
            this._cdev.mv(offset= 0.0-offset)
            return 1
        else:
            print this.stack()
            print tstsaektl
            return 0

    def haste(this):
        return this.el._oldhaste

    def now(this):
        return this.el.time
    def time(this):
        if this._cdev != 0:
            return this._cdev.time
        else:
            return None

    def last(this):
        if this._cdev != 0:
            return this._cdev.time - this.el.time
        return 0



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


