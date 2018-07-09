from __init__ import Spell

class Kegsmash(Spell):
    config = {
        "cd":8,
        "stackmax":1,
        "hashaste":1,
        "_END":0
    }
    def effect(this):
        brm = this.src
        brm.brew.reduce(4)


class Brew(Spell):
    config = {
        "cd":12,
        "stackmax":3,
        "hashaste":1,
        "_END":0
    }
    pass


class a():
    ks = Kegsmash(this)
    brew = Brew(this)


def main():
    a = 

if __name__ == "__main__" :
    main()


