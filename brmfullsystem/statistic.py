
class statisunit(object):
    __value = 0
    __unitname = 'nil'
    __src = 'null'
    __parent = 0
    __count = 0

    def __init__(this,p,src = 'null'):
        this.__parent = p
        this.__unitname = p.unitname
        this.__src = src

    def __iadd__(this,other):
        this.__value += other
        this.__count += 1
        this.__parent.value += other
        this.__parent.count += 1
        this.__parent.getv()[this.__unitname] += other
        return this

    def __str__(this):
        return str(this.__value)
    def __impr__(this):
        return str(this.__value)
    def getc(this):
        return this.__count
    def value(this):
        return this.__value
        
    def getp(this):
        return this.__parent



class statistic(object):
    unitname = 'nil'
    __values = {}
    __counts = {}
    allunits = {}
    allsrcs = {}

    def __new__(this,unitname='nil'):
        if unitname in this.allunits :
            return this.allunits[unitname]
        else:
            return object.__new__(statistic)

    def __init__(this,unitname='nil'):
        this.unitname = unitname
	if unitname not in this.__values :
	    this.__values[unitname] = 0
	if unitname not in this.allunits :
	    this.allunits[unitname] = this

        this.allunits[unitname] = this
        this.value = 0
        this.count = 0
        this.srcs= {}

    def __getattr__(this,name):
        if '__values' in name :
            print 'err getattr'
            print cast
        if name not in this.__dict__:
	    src = name
            tmp = statisunit(this,name)
            setattr(this,name,tmp)

	    if src not in this.srcs:
		this.srcs[src] = tmp

	    if src not in this.allsrcs:
		this.allsrcs[src] = [this]
	    else:
		this.allsrcs[src].append(this)
        return super(statistic,this).__getattribute__(name)

    def __str__(this):
        tmp = 'statis unit="%s"'%this.unitname
        return tmp

    def getv(this):
        return this.__values

    def get(this,unit,src):
        return this.units[unit].__getattr__(src)

    def gets(this,name):
        return this.__getattr__(name)
	
    def clean(this) :
	#print this.__dict__
	attrname = []
	for i in this.__dict__ :
	    attrname.append(i)   
	for i in attrname:
	    this.__delattr__(i)

	this.__values = {}
	this.__counts = {}
	this.allunits = {}
	this.allsrcs = {}
        statistic.allunits = {}
        statistic.allsrcs = {}
        statistic.__values = {}
        statistic.__counts = {}
        this.value = 0
        this.count = 0
        this.srcs= {}
	#exit()

    def showunit(this):
        ret = ''
        for i in this.allunits :
            #print i
            #print this.allunits[i].srcs
            #print this.allunits[i].allsrcs
            #return

            ret += '%s>_\t\n'%i
            print '%s>_\t'%i
            s = this.allunits[i].srcs
            for j in s :
                #print j,
                srcname = j
                value = s[j].value()
                sumvalue = s[j].getp().value
                count = str(s[j].getc())
                if value >= 1000000:
                    print '\t%s: %dm(%.2f%%) | %s hits'%(srcname,value/1000000,float(value)/sumvalue*100,count)
                    ret += '\t%s: %dm(%.2f%%) | %s hits\n'%(srcname,value/1000000,float(value)/sumvalue*100,count)
                elif value >= 10000 :
                    print '\t%s: %dw(%.2f%%) | %s hits'%(srcname,value/10000,float(value)/sumvalue*100,count)
                    ret += '\t%s: %dw(%.2f%%) | %s hits\n'%(srcname,value/10000,float(value)/sumvalue*100,count)
                else :
                    print '\t%s: %d(%.2f%%) | %s hits'%(srcname,value,float(value)/sumvalue*100,count)
                    ret += '\t%s: %d(%.2f%%) | %s hits\n'%(srcname,value,float(value)/sumvalue*100,count)
            print ''
            ret += '\n'
        return ret



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
