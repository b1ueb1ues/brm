class config(object):

    dic = 0
    stat = [0,0,0,0]

    def __init__(this,transfer=0, **argv):
        if transfer != 0 :
            transfer.update(argv)
            argv = transfer
        this.stat = [25,25,0,25]
        for a in argv:
            this.__setattr__(a,argv[a])
        return

    def __setattr__(this,name,value):
        if name == 'crit' :
            this.stat[0] = value
        elif name == 'haste' :
            this.stat[1] = value
        elif name == 'vers' :
            this.stat[2] = value
        elif name == 'mastery' :
            this.stat[3] = value
        elif name == 'stat' :
            this.crit = value[0]
            this.haste = value[1]
            this.vers = value[2]
            this.mastery = value[3]
        super.__setattr__(this,name,value)

    def setup(this,target):
        dic = this.__dict__
        for i in dic :
            if i == 'haste' :
                h = float(dic[i])
                target.__setattr__(i,h/100+1)
            elif i == 'crit' :
                c = float(dic[i])
                target.__setattr__(i,c/100)
            elif i == 'vers' :
                v = float(dic[i])
                target.__setattr__(i,v/100)
            elif i == 'mastery' :
                m = float(dic[i])
                target.__setattr__(i,m/100)
            else:
                target.__setattr__(i,dic[i])


    def show(this):
        dic = this.__dict__
        print '--------------------'
        for i in dic :
            if i == 'stat' :
                print 'stat: [%.2f, %.2f, %.2f/%.2f, %.2f]'%(dic[i][0],dic[i][1],dic[i][2],float(dic[i][2])/2,dic[i][3])
            elif i == 'crit' :
                pass
            elif i == 'haste' :
                pass
            elif i == 'vers' :
                pass
            elif i == 'mastery' :
                pass
            else:
                print '%s: %s'%(i,dic[i])

        print '--------------------'


def main():


    a = {'equip':['4t'],
        'talent':['black','ht15'],
        'iduration':8.5,
        'haste':30,
        }
    c = config(transfer=a)
    c.show()
    exit()
    c.show()
    c.stat = [25,25,11,25]
    c.show()

if __name__ == "__main__" :
    main()
