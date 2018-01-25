class Proc(object):
    def __init__(this,clk):
        this.clock = clk
        this.iv = clk.iv
        this._init()

    def _init(this):
        pass

    def tick(this):
        print 'Proc base tick'
        pass
        

class Clock(object):
    def __init__(this):
        this.now = 0
        this.longest = 1000 * 1000
        this.iv = 1
        this.proctick = []
        this.proc = {}
        this._log = []

    def log(this, logstr):
        this._log.append(logstr)

    def printlog(this):
        print '------------------'
        print '---logstart-------'
        for i in this._log:
            print i

    def run(this):
        while this.now <= this.longest :
            if this.now in this.proc:
                proclist_now = this.proc.pop(this.now)
                for i in proclist_now :
                    i.tick()
            i = 0
            for i in this.proctick :
                i.tick()

            if not i : #tickproc is empty
                i = 0
                for i in this.proc: 
                    this.now = i
                if not i : #proc is empty
                    #print 'clock empty'
                    return 
            else:
                this.now += this.iv

    def stop(this):
        this.longest = this.now

    def add(this,p,time=-1):
        if time == -1 :
            this.proctick.append(p)
        else :
            if time in this.proc :
                this.proc[time].append(p)
            else:
                this.proc[time] = [p]



def main():

    a = Clock()
    b = Aura(a)
    b.on()
    a.run()
    print b._test

if __name__ == "__main__":
    main()

