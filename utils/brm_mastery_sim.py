import random
random.seed(0)


class Brm(object):
    dodgebase = 0.1
    def __init__(this):
        this.eb_stack = 0
        this.hit = 0
        this.dodge = 0
        this.mastery = 0.08

    def reset(this):
        this.eb_stack = 0
        this.hit = 0
        this.dodge = 0

    def dt(this):
        r = random.random()
        dodge_rate = this.eb_stack * this.mastery + this.dodgebase
        if r < dodge_rate :
            this.dodge += 1
            this.eb_stack = 0
        else:
            this.hit += 1
            this.eb_stack += 1

    def bos(this):
        this.eb_stack += 1

    def run(this, mastery):
        this.reset()
        this.mastery = mastery
        for i in range(1000000):
            i = i/2.0
            if i % 1.5 < 0.5:
                this.dt()
            if i % 3 < 0.5:
                this.bos()

def main():
    b = Brm()
    i = 0.08 - 0.01
    o_dmg_avoid = 0
    dodgebase = b.dodgebase

    while i<0.7 :
        i += 0.01
        b.run(i)
        dodge_avg = 1.0 * b.dodge/(b.dodge+b.hit)
        print "%.2f, %.4f"%(i, dodge_avg)

        dmg_avoid = 1 - (1-dodge_avg) / (1 - dodgebase)
        if o_dmg_avoid == 0:
            o_dmg_avoid = dmg_avoid
            continue
    
        print "attack dmg avoid:", dmg_avoid
        print "attack dmg avoid than before :", 1-(1-dmg_avoid)/(1-o_dmg_avoid)
        a = 1-(1-dmg_avoid)/(1-o_dmg_avoid)
        print ''
        o_dmg_avoid = dmg_avoid 


if __name__ == "__main__":
    main()


