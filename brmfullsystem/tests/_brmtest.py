#if __name__ == '__main__' and __package__ is None:
if __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from brmfs import *
import copy

def main():

    '''
    confdefault = config(stat=[25,25,0,27],equip=['4t'],talent=['black','ht15'],iduration=8.5,palmcdr=1.3, haste=0, crit=0, vers=0, mastery=0)
    '''

    pool = []

    pool.append(brm( \
        equip=[],talent=['light','ht'],stat=[25,25,0,25]   \
        ))

    #test2haste(pool)
    #testhaste(pool)
    teststat(pool,statindex=1)

def test2haste(pool, time = 100000, start = 10, stop = 40, offset = 0.02):
    if len(pool) != 2:
        print ' pool != 2 '
        exit()
    i = start - offset
    col = 1
    for l in pool:
        print '%d: '%col,
        col += 1
        l.show()
    print '\nhaste\t1\t2\tdiff\t'
    while(1):
        i += offset
        print i
        if i > stop+0.01 :
            break
        av = []
        pool[0].haste = i
        pool[1].haste = i
        a = pool[0]
        b = pool[1]
        a.run(time)
        b.run(time)
        ar = float(a.getehrr())
        br = float(b.getehrr())
        d = 1.0-(1.0-ar)/(1.0-br)
        flag = 1
        if d < 0 :
            flag = 2
            d = 1.0-(1.0-br)/(1.0-ar)

        hasteprint = i
        print "%.0f%%"%hasteprint,
        print '\t%.4f\t%.4f\t%.4f'%(float(ar),float(br),float(d))


def test2(pool, time = 100000):
    if len(pool) != 2:
        print ' pool != 2 '
        exit()
    a = pool[0]
    b = pool[1]
    a.run(time)
    b.run(time)
    ar = a.showavoid()
    print '>'
    br = b.showavoid()
    d = 1-(1-ar)/(1-br)
    flag = 1
    if d < 0 :
        flag = 2
        d = 1-(1-br)/(1-ar)
    print '\n>\ndiff:',d,'%d better'%flag

def testn(line, time = 100000,basebrm=0):

    if basebrm != 0:
        print 'base:',
        basebrm.show()

    col = 1
    for l in line:
        print '%d: '%col,
        col += 1
        l.show()

    print '\n>'
    basebrm.run(time)
    base = basebrm.getehrr()
    print 'base:',base
    for j in range(len(line)):
            print '%d\t'%(j+1),
    print ''

    
    av = []
    for c in line :
        b = c 
        b.run(time)
        av.append(b.getehrr())
        #print av


    for a in av:
        print '%.4f\t'%float(a),
    print ''
    if basebrm != 0:
        for a in av:
            print '%.4f\t'%(1-(1-a)/(1-base)),
        print ''

def teststatwide(line, time = 100000, start = 10, stop = 40, offset = 2, statindex=1):

    stop += 5
    i = start - offset

    col = 1
    for l in line:
        print '%d: '%col,
        col += 1
        l.show()

    if statindex == 0:
        print '\ncrit\t',
    elif statindex == 1:
        print '\nhaste\t',
    elif statindex == 2:
        print '\nvers\t',
    elif statindex == 3:
        print '\nmastery\t',

    for j in range(len(line)):
        print '%d\t'%(j+1),
    print ''
    allav = []
    while(1):
        i += offset
        if i > stop :
            break
        av = []
        for c in line :
            b = copy.deepcopy(c)
            b.initargv['stat'][statindex] = i
            b.run(time)
            av.append(b.getehrr())
            #print av

        allav.append(av)

        if len(allav) >= 6:
            print "%d%%"%(i-5*offset),
            index = 0
            av = allav[-6]
            for a in av:
                aplus = allav[-5][index]
                da = (1-(1-a)/(1-aplus))
                da_ave = da
                for j in range(4):
                    aplus = allav[-1-j][index]
                    da = (1-(1-aplus)/(1-a))
                    da_ave += da
                da_ave = da_ave/5
                print '\t%.4f | %.4f'%(float(a),da_ave),
                index += 1
            print ''
def teststat(line, time = 100000, start = 10, stop = 40, offset = 2, statindex=1):

    i = start - offset

    col = 1
    for l in line:
        print '%d: '%col,
        col += 1
        l.show()

    if statindex == 1:
        print '\nhaste\t',
    elif statindex == 0:
        print '\ncrit\t',
    elif statindex == 2:
        print '\nvers\t',
    elif statindex == 3:
        print '\nmastery\t',

    for j in range(len(line)):
        print '%d\t'%(j+1),
    print ''
    allav = []
    while(1):
        i += offset
        if i > stop :
            break
        av = []
        for c in line :
            c.initargv['stat'][statindex] = i
            b = copy.deepcopy(c)
            b.run(time)
            av.append(b.getehrr())
            #print av

        print "%d%%"%(i),
        index = 0
        for a in av:
            if len(allav) >= 1:
                a_old = allav[-1][index]
            else :
                a_old = 0
            print '\t%.4f | %.4f'%(float(a),1-(1-a)/(1-a_old)),
            index += 1
        allav.append(av)
        print ''



if __name__ == "__main__":
    main()
