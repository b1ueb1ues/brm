from brm import *



def main():
    average = 1


    offset = 0.01
    i = 1.0 - offset
    old = 0

    init = 0

    while(1):
        i += offset
        if i > 1.5 :
            break

        d = brm(haste=i,equip=['4t'],talent=['black','ed'],mastery = 0.3, iduration = 9)
        d.run(100000)

        if init == 0 :
            a = d.getmavoid()
            loc = a.find('|')
            if loc != -1 :
                a = a[:loc]
            base = float(a)
            init = 1
            continue

        print "%2d%%\t"%((i-1)*100),

        print '%s\t'%(d.getmavoid()),

        a = d.getmavoid()
        loc = a.find('|')
        if loc != -1 :
            a = a[:loc]

        avoidance = float(a)
        tmp = 1-(1-avoidance)/(1-base)
        print '> %.4f'%(tmp/(i-1)),

        print ' '

        if average == 0 :
            base = tmp
#}main()



if __name__ == '__main__' :
    main()
