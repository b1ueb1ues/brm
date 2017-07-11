from brm import *

f = open("figure/figure_mastery.csv",'w')


def main(typ = 'ave', time = 100000):
    average = 1
    global f


    offset = 0.01
    i = 0.08 - offset
    old = 0.01

    init = 0

    while(1):
        i += offset
        if i > 0.45 :
            break

        d = brm(haste=1.25,equip=['4t'],talent=['black','ht15'],mastery = i, iduration = 8.5, newfuzan = 1)
        d.bsmastery = 0
        d.fbmastery = 0
        d.run(time)

        if init == 0 :
            a = d.getehrr()
            base = float(a)
            old = base
            init = 1
            continue

        print "%2.0f%%\t"%((i)*100),

        print '%s\t'%(d.getehrr()),

        a = d.getehrr()

        avoidance = float(a)
        tmp = 1-(1-avoidance)/(1-base)
        tmp2 = 1-(1-avoidance)/(1-old)
        #print avoidance,old
        old = avoidance
        print '> %.4f (%.4f)'%(tmp/(i-0.08),tmp2*100),
        if typ == 'ave':
            f.write('%.4f,'%(tmp/(i-0.08)))
        else :
            f.write('%.4f,'%(tmp2*100))

        print ' '

        if average == 0 :
            base = tmp
    f.write('\n')
#}main()



if __name__ == '__main__' :
    main('point')
    exit()
    for i in range(10):
        main('point',time = i * 10000 + 10000)
