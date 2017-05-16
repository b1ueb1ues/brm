
class statisunit(object):
    __value = 0
    __name = 'null'
    __parent = 0

    def __init__(this,p,n = 'null'):
        this.__parent = p
        this.__name = n
        if this.__name not in this.__parent.getv() :
            this.__parent.getv()[this.__name] = this.__value

    def __iadd__(this,other):
        this.__value += other
        this.__parent.getv()[this.__name] += other
        print this.__parent.getv()
        return this

    def __str__(this):
        return str(this.__value)
    def __impr__(this):
        return str(this.__value)
        



class statistic(object):
    src = 'null'
    __values = {}
    instance = []

    def __init__(this,src='null'):
        this.src = src
        this.instance.append(this)

    def __getattr__(this,name):
        if '__values' in name :
            print 'err getattr'
            print cast
        if name not in this.__dict__:
            tmp = statisunit(this,name)
            super(statistic,this).__setattr__(name,tmp)
        return getattr(this,name)

    def __str__(this):
        tmp = 'statis from src="%s"'%this.src
        return tmp

    def getv(this):
        return this.__values
            


def main():
    a = statistic(src='1')
    a.st += 3
    a.test += 4

    b = statistic(src='2')
    b.st += 4

    for i in statistic.instance:
        print i,i.st,i.test


if __name__ == '__main__' :
    main()
