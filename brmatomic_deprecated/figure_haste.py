from brm import *

f = open("figure/figure_haste.csv",'w')


def main(typ = 'ave', time = 100000):
    average = 1
    global f


    offset = 400.0/37500
    i = 1.0 - offset
    old = 0.01

    init = 0

    while(1):
        i += offset
        if i > 1.5 :
            break

        d = brm(haste=i,equip=['4t'],talent=['black','ht15'],mastery = 0.3, iduration = 8.5, newfuzan = 1)
        d.run(time)

        if init == 0 :
            a = d.getehrr()
            base = float(a)
            old = base
            init = 1
            continue

        print "%2d%%\t"%((i-1)*100),

        print '%s\t'%(d.getehrr()),

        a = d.getehrr()

        avoidance = float(a)
        tmp = 1-(1-avoidance)/(1-base)
        tmp2 = 1-(1-avoidance)/(1-old)
        old = avoidance
        print '> %.4f (%.4f)'%(tmp/(i-1),tmp2*100),
        if typ == 'ave':
            f.write('%.4f,'%(tmp/(i-1)))
        else :
            f.write('%.4f,'%(tmp2*100))

        print ' '

        if average == 0 :
            base = tmp
    f.write('\n')
#}main()



if __name__ == '__main__' :
    main('point')
    main('ave')
    exit()
    for i in range(10):
        main('point',time = i * 10000 + 10000)
