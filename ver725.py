#if __name__ == '__main__' and __package__ is None:
if __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from brm import *

def main():

    '''
    confdefault = config(stat=[25,25,0,27],equip=['4t'],talent=['black','ht15'],iduration=8.5,palmcdr=1.3, haste=0, crit=0, vers=0, mastery=0)
    '''

    pool = []

    pool.append(config(\
        stat=[30,25,0,20],equip=['2t'],talent=['black','ht15']   \
        ))
    pool.append(config( \
        stat=[30,31,0,20],equip=[''],talent=['black','ht15']   \
        ))

    #test2haste(pool)
    #testhaste(pool)
    test2(pool)

def test2haste(pool, time = 100000, start = 1.1, stop = 1.4, offset = 0.02):
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
        a = brm(conf = pool[0])
        b = brm(conf = pool[1])
        a.run(time)
        b.run(time)
        ar = float(a.getehrr())
        br = float(b.getehrr())
        d = 1.0-(1.0-ar)/(1.0-br)
        flag = 1
        if d < 0 :
            flag = 2
            d = 1.0-(1.0-br)/(1.0-ar)

        hasteprint = (100*i-100)
        print "%.0f%%"%hasteprint,
        print '\t%.4f\t%.4f\t%.4f'%(float(ar),float(br),float(d))


def test2(pool, time = 100000):
    if len(pool) != 2:
        print ' pool != 2 '
        exit()
    a = brm(conf = pool[0])
    b = brm(conf = pool[1])
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
    print '\n>\ndiff:',d,'%d good'%flag

def testn(line, time = 100000):

    col = 1
    for l in line:
        print '%d: '%col,
        col += 1
        l.show()

    print '\n>'
    for j in range(len(line)):
        print '%d\t'%(j+1),
    print ''

    av = []
    for c in line :
        b = brm(conf=c)
        b.run(time)
        av.append(b.getehrr())
        #print av

    for a in av:
        print '%.4f\t'%float(a),
    print ''

def testhaste(line, time = 100000, start = 1.1, stop = 1.4, offset = 0.02):

    i = start - offset
    col = 1
    for l in line:
        print '%d: '%col,
        col += 1
        l.show()

    print '\nhaste\t',
    for j in range(len(line)):
        print '%d\t'%(j+1),
    print ''
    while(1):
        i += offset
        if i > stop :
            break
        av = []
        for c in line :
            c.haste = i
            b = brm(conf=c)
            b.run(time)
            av.append(b.getehrr())
            #print av

        print "%d%%"%(100*(i-1)),
        for a in av:
            print '\t%.4f'%float(a),
        print ''



if __name__ == "__main__":
    main()
