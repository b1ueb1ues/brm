
class statistic(object):
    s_value = [0]
    src = 'null'

    addcount = 0
    subcount = 0
    addsum = 0
    subsum = 0
    s_addcount = [0]
    s_subcount = [0]
    s_addsum = [0]
    s_subsum = [0]

    def __init__(this,src='null'):
        this.src = src


    def get(this):
        return this.s_value[0]


    def add(this,value):
        this.s_value[0] += value
        this.addcount += 1
        this.s_addcount[0] += 1
        this.addsum += value
        this.s_addsum[0] += value

    def sub(this,value):
        this.s_value[0] -= value
        this.subcount += 1
        this.s_subcount[0] += 1
        this.subsum += value
        this.s_subsum[0] += value

    def set(this,newvalue):
        diff = newvalue - this.get()
        if diff > 0 :
            this.add(diff)
        elif diff < 0 :
            this.sub(0-diff)



    def __add__(this,other):
        return this.get() + other
    def __radd__(this,other):
        return this.get() + other
    def __iadd__(this,other):
        this.add(other)
        return this

    def __sub__(this,other):
        return this.get() - other
    def __rsub__(this,other):
        return this.get() - other
    def __isub__(this,other):
        this.sub(other)
        return this

    def __str__(this):
        return str(this.get())

    def addstatistic(this):
        pass
    def show(this):
        pass

    


def main():
    class test(statistic):
        'test'
    a = test()
    b = test()
    a.set(4)
    b += 5
    a.set(-3)
    b -= 2

    print a.get()
    print a.addsum,b.addsum
    print a.subsum,b.subsum

if __name__ == '__main__' :
    main()
