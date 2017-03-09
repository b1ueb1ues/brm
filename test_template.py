from brm import *

def main():

    '''
    confdefault = config(stat=[25,25,0,27],equip=['4t'],talent=['black','ht15'],iduration=8.5,palmcdr=1.3, haste=0, crit=0, vers=0, mastery=0)
    '''

    pool = []

    pool.append( config(equip=['4t']) )
    pool.append( config(equip=['4t','ring','waist']) )

    testhaste(pool)


def testhaste(line):

    offset = 0.02
    start = 1.1
    stop = 1.4
    i = start - offset
    col = 1
    for l in line:
        print '%d: '%col,
        col += 1
        l.show()
    print '\nhaste\t1\t2\t'
    while(1):
        i += offset
        if i > stop :
            break
        av = []
        for c in line :
            c.haste = i
            b = brm(conf=c)
            b.run(100000)
            av.append(b.getmavoid())
            #print av

        print "  %d%%"%(100*(i-1)),
        for a in av:
            print '\t%.4f'%float(a),
        print ''

        




if __name__ == "__main__":
    main()
