from _brmtest import *

def main():
    average = 1


    offset = 0.01
    i = 1.2 - offset
    old = 0

    init = 0

    d = brmtest(haste=1.3,equip=['4t'],talent=['black','ed20'],mastery = 0.3, iduration = 9)
    d.run(100000)
    d.showavoid()

    d = brm(haste=1.3,equip=['4t'],talent=['black','ed20'],mastery = 0.3, iduration = 9)
    d.run(100000)
    d.showavoid()
    exit()
    while(1):
        i += offset
        if i > 1.5 :
            break

        d = brmtest(haste=i,equip=['4t'],talent=['black','ed20'],mastery = 0.3, iduration = 9)
        d.run(100000)

        if init == 0 :
            a = d.getmavoid()
            loc = a.find('|')
            if loc != -1 :
                a = a[:loc]
            base = float(a)
            init = 1
            continue

        print "%2d%%\t"%((i-1)*100),

        print '%s\t'%(d.getmavoid()),

        a = d.getmavoid()
        loc = a.find('|')
        if loc != -1 :
            a = a[:loc]

        avoidance = float(a)
        tmp = 1-(1-avoidance)/(1-base)
        print '> %.4f'%(tmp/(i-1)),

        print ' '

        if average == 0 :
            base = tmp
#}main()



class brmtest(brm):
    class BlackEv(RepeatEvent):
        def repeatproc(this):
            this.ironskin=1
            this.src.fish()
            this.src.blackgain += 1
            n = this.src.brewstack + 1
            this.src.brewcdev.move(newtiming = this.el.time + this.src.brewcd)
            this.src.brewstack = this.src.brewstackmax - 1
            this.src.ironcount += n
            this.src.brewgain += 3
            tmpev = brm.PalmEv(this.src,repeat=0)
            tmpev.time = this.time + 0.01
            tmpev.addto(this.el)
            tmpev = brm.PalmEv(this.src,repeat=0)
            tmpev.time = this.time + 0.02
            tmpev.addto(this.el)

            a = brmtest.IronEv(this.src,repeat = 0)
            a.time = this.time + n*this.src.iduration
            a.addto(this.el)

    class IronEv(RepeatEvent):
        def repeatproc(this):
            this.src.ironskin = 0
            return

    def __init__(this,conf=0,talent=['black','ht'],equip=['ring','waist'], \
            iduration = 8, palmcdr = 1.3, haste = 1.3, dodgebase = 0.10, mastery = 0, crit = 0, vers = 0, meleetakeiv = 1.5 ):

        brm.__init__(this, conf,talent, equip, iduration, palmcdr, haste, dodgebase, mastery, crit, vers)

        this.el.rm(this.ironev)
        this.el.rm(this.blackev)
        this.blackev = brmtest.BlackEv(this, repeat = 90)
        this.el.add(this.blackev)

        

if __name__ == "__main__" :
    main()


