from __init__ import Spell

class Mr(Spell):
    config = {
        "cd":0,
        "stackmax":1,
        "hashaste":0,
        "cost"     : {"rune":2} ,
        "channel"  : 0  ,
        "cast"     : 0  ,
        "_END":0
    }
    def check(this):
        bdk = this.src
        cost = this.config['cost']
        if cost != {}:
            for i in cost:
                if bdk.resouces[i] < cost[i]
                return 0
        return 1
        
    def effect(this):
        bdk = this.src
        if this.check():
            bdk.bs = 3
            bdk.userune()

class Ds(Spell):
    config = {
        "cd":0,
        "stackmax":1,
        "hashaste":0,
        "_END":0
    }
    def check(this):
        bdk = this.src
        if bdk.rune >= 2:
            return 1
        else:
            return 0
        
    def effect(this):
        if this.check():
            bdk = this.src

            
            }

class Brew(Spell):
    config = {
        "cd":12,
        "stackmax":3,
        "hashaste":1,
        "_END":0
    }
    pass


class A():
    def __init__(this):
        this.ks = Kegsmash(this)
        this.brew = Brew(this)


def main():
    a = A()
    a.ks.cast()

if __name__ == "__main__" :
    main()


