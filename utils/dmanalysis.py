
def foo(x,k):
    x = float(x)
    k = float(k)
    return x/(x+k)

def dr2ehp(x):
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

    print 'brm stagger, ',
    f.write('铁骨欠债, ')
    for i in range(tick):
        a = i * iv + statbase
        a = a*3.5
        print '%.2f, '%(dr2ehp(srate(a))/0.7),
        f.write('%.2f, '%(dr2ehp(srate(a))/0.7))
    print ''
    f.write('\n')




    print 'brm dm',
    f.write('保持铁骨(平均收益,30急速后), ')
    for i in range(tick):
        a = i * iv + statbase
        a = a*3.5
        print '%.2f, '%(dr2ehp(srate(a)*0.35)/0.7),
        f.write('%.2f, '%(dr2ehp(srate(a)*0.35)/0.7))
    print ''
    f.write('\n')

    print 'brm dm noisb',
    f.write('活tm的(平均收益), ')
    for i in range(tick):
        a = i * iv + statbase
        print '%.2f, '%(dr2ehp(srate(a)*0.5)/0.7),
        f.write('%.2f, '%(dr2ehp(srate(a)*0.5)/0.7))
    print ''
    f.write('\n')

    print 'brm dm 1i1p, ',
    f.write('1铁1活, ')
    for i in range(tick):
        a = i * iv + statbase
        a = a*3.5
        print '%.2f, '%(dr2ehp(srate(a)*0.5)/0.7),
        f.write('%.2f, '%(dr2ehp(srate(a)*0.5)/0.7))
    print ''
    f.write('\n')

    print 'brm dm 1i2p, ',
    f.write('1铁2活, ')
    for i in range(tick):
        a = i * iv + statbase
        a = a*3.5
        print '%.2f, '%(dr2ehp(srate(a)*0.75)/0.7),
        f.write('%.2f, '%(dr2ehp(srate(a)*0.75)/0.7))
    print ''
    f.write('\n')


    print 'dk,', 
    f.write('骨盾, ')
    for i in range(tick):
        s = i * iv + statbase
        print '%.2f, '%(dr2ehp(dkrate(s))),
        f.write('%.2f, '%(dr2ehp(dkrate(s))))
    print ''
    f.write('\n')


    print 'pala,', 
    f.write('炖鸡, ')
    for i in range(tick):
        s = i * iv + statbase
        print '%.2f, '%(dr2ehp(palarate(s))),
        f.write('%.2f, '%(dr2ehp(palarate(s))))
    print ''
    f.write('\n')


    f.close()


if __name__ == '__main__':
    main()


