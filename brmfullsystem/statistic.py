
class statisunit(object):
    __value = 0
    __unitname = 'nil'
    __src = 'null'
    __parent = 0

    def __init__(this,p,src = 'null'):
        this.__parent = p
        this.__unitname = p.unitname
        this.__src = src
        if this.__unitname not in this.__parent.getv() :
            this.__parent.getv()[this.__unitname] = this.__value
        if this.__unitname not in this.__parent.allunits :
            this.__parent.allunits[this.__unitname] = this.__parent

        if this.__src not in this.__parent.srcs :
            this.__parent.srcs[this.__src] = this

        if this.__src not in this.__parent.allsrcs:
            this.__parent.allsrcs[this.__src] = [this.__parent]
        else: 
            this.__parent.allsrcs[this.__src].append(this.__parent)

        #else :
        #    this.__parent.units[this.__name].append(this.__parent)

    def __iadd__(this,other):
        this.__value += other
        this.__parent.value += other
        this.__parent.getv()[this.__unitname] += other
        print 'iadd',this.__parent.getv()
        return this

    def __str__(this):
        return str(this.__value)
    def __impr__(this):
        return str(this.__value)
        



class statistic(object):
    unitname = 'nil'
    __values = {}
    allunits = {}
    allsrcs = {}
    srcs= {}

    def __new__(this,unitname='nil'):
        if unitname in this.allunits :
            return this.allunits[unitname]
        else:
            return object.__new__(statistic)

    def __init__(this,unitname='nil'):
        this.unitname = unitname
        this.allunits[unitname] = this
        this.value = 0

    def __getattr__(this,name):
        if '__values' in name :
            print 'err getattr'
            print cast
        if name not in this.__dict__:
            tmp = statisunit(this,name)
            setattr(this,name,tmp)
        return super(statistic,this).__getattribute__(name)

    def __str__(this):
        tmp = 'statis unit="%s"'%this.unitname
        return tmp

    def getv(this):
        return this.__values

    def get(this,unit,src):
        return this.units[unit].__getattr__(src)

    def showunit(this):
        ret = ''
        for i in this.units :
            ret += '%s>_'%i
            print '%s>_'%i,
            for j in i :
                srcname = j.src
                value = getattr(j,i)
                print '%s: %.2f'%(srcname,value)



def main():
    st = statistic('st')
    st2 = statistic('st')
    c = statistic('test')

    st.a += 2
    st2.a += 3
    st.b += 4
    c.a += 5
    print st,st.a,st.b
    print '------'
    print st.srcs
    print st.allsrcs
    


if __name__ == '__main__' :
    main()
