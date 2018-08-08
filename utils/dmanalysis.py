
def foo(x,k):
    x = float(x)
    k = float(k)
    return x/(x+k)

def ehp(x):
    return 1.0/(1.0-x)

def srate(a):
    return foo(a, 6300.0/1.4)

def dkrate(s):
    return foo(s*0.4+6300, 6300)

def palarate(s):
    return foo(s*1.5+6300, 6300)

def main():
    f = open('ehp.csv','wb')

    tick = 31
    statbase = 4000
    iv = 200

    print 'main stat, ',
    f.write('main stat, ')
    for i in range(tick):
        a = i * iv + statbase
        print '%d, '%(a),
        f.write('%d, '%(a))
    print ''
    f.write('\n')




    print 'brm dm noarmor, ',
    f.write('brm dm noarmor, ')
    for i in range(tick):
        a = i * iv + statbase
        a = a*3.5
        print '%.2f, '%(ehp(srate(a)*0.35)),
        f.write('%.2f, '%(ehp(srate(a)*0.35)))
    print ''
    f.write('\n')

    print 'brm dm 1i1p, ',
    f.write('brm dm 1i1p, ')
    for i in range(tick):
        a = i * iv + statbase
        a = a*3.5
        print '%.2f, '%(ehp(srate(a)*0.5)/0.7),
        f.write('%.2f, '%(ehp(srate(a)*0.5)/0.7))
    print ''
    f.write('\n')

    print 'brm dm 1i2p, ',
    f.write('brm dm 1i2p, ')
    for i in range(tick):
        a = i * iv + statbase
        a = a*3.5
        print '%.2f, '%(ehp(srate(a)*0.75)/0.7),
        f.write('%.2f, '%(ehp(srate(a)*0.75)/0.7))
    print ''
    f.write('\n')


    print 'dk,', 
    f.write('dk, ')
    for i in range(tick):
        s = i * iv + statbase
        print '%.2f, '%(ehp(dkrate(s))),
        f.write('%.2f, '%(ehp(dkrate(s))))
    print ''
    f.write('\n')


    print 'pala,', 
    f.write('pala, ')
    for i in range(tick):
        s = i * iv + statbase
        print '%.2f, '%(ehp(palarate(s))),
        f.write('%.2f, '%(ehp(palarate(s))))
    print ''
    f.write('\n')

    print 'brm stagger, ',
    f.write('brm stagger, ')
    for i in range(tick):
        a = i * iv + statbase
        a = a*3.5
        print '%.2f, '%(ehp(srate(a))),
        f.write('%.2f, '%(ehp(srate(a))))
    print ''
    f.write('\n')


    f.close()


if __name__ == '__main__':
    main()


