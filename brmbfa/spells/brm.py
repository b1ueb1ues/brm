from __init__ import Spell

class Kegsmash(Spell):
    config = {
        "cd":8,
        "stack_max":1,
        "has_haste":1,
        "cost":{'energy':40},
        "_END":0
    }
    def effect(this):
        brm = this.src
        brm.brew.reduce(4)


class Brew(Spell):
    config = {
        "cd":12,
        "stack_max":3,
        "has_haste":1,
        "_END":0
    }

class TP(Spell):
    config = {
        'cost':{'energy':25},
        "_END":0
    }


class A():
    def __init__(this):
        this.ks = Kegsmash(this)
        this.brew = Brew(this)


def main():
    a = A()
    a.ks.cast()

if __name__ == "__main__" :
    main()


