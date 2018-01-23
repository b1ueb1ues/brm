class Proc(object):
    def __init__(this,clk):
        this.clock = clk
        this.iv = clk.iv

    def tick(this):
        print 'Proc base tick'
        pass
        
class Aura(Proc):
    def __init__(this,clk):
        super(Aura,this).__init__(clk)
        this.enable = 0
        this.duration = 6000
        this._test = 0

    def on(this):
        this.start = this.clock.now
        this.enable = 1
        this.clock.add(this,this.start + this.duration)

    def off(this):
        this.enable = 0


    def tick(this):
        this._test = this.clock.now
        this.off()



class Clock(object):
    def __init__(this):
        this.now = 0
        this.longest = 1000 * 1000
        this.iv = 1
        this.proctick = []
        this.proc = {}


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
    a = {}
    for i in a:
        print a.pop(i)
    a[5] = 5
    a[3] = 3
    a[7] = 7
    print a.pop(6)
    exit()

    print a
    for i in a:
        a[8] = 8
        print i
        break
    exit()


    a = Clock()
    b = Aura(a)
    b.on()
    a.run()
    print b._test

if __name__ == "__main__":
    main()

