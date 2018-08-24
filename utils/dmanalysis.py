# -*- encoding:utf8 -*-
from pbratelite import *
from brm_bps import *

def foo(x,k):
    x = float(x)
    k = float(k)
    return x/(x+k)

def dr2ehp(x):
    return 1.0/(1.0-x)

def srate(a):
    return foo(a, 6300.0/1.4)

def dkrate(s):
    abase = 4500
    return foo(s*0.4+abase, 6300)

def palarate(s):
    abase = 4500
    return foo(s*1.5+abase, 6300)

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
        print '%.2f, '%(dr2ehp(srate(a))/0.8),
        f.write('%.2f, '%(dr2ehp(srate(a))/0.8))
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

    print 'brm dm 1i2p, ',
    f.write('1铁2活, ')
    for i in range(tick):
        a = i * iv + statbase
        a = a*3.5
        print '%.2f, '%(dr2ehp(srate(a)*0.7)/0.8),
        f.write('%.2f, '%(dr2ehp(srate(a)*0.7)/0.8))
    print ''
    f.write('\n')


#    print 'brm dm',
#    f.write('保持铁骨(平均收益,30急速后), ')
#    for i in range(tick):
#        a = i * iv + statbase
#        a = a*3.5
#        print '%.2f, '%(dr2ehp(srate(a)*0.35)/0.7),
#        f.write('%.2f, '%(dr2ehp(srate(a)*0.35)/0.7))
#    print ''
#    f.write('\n')

    print 'brm dm noisb',
    f.write('活tm的(平均收益), ')
    piv = 1.0/bps(1.2,t3='lb')
    _prate = prate(piv)
    for i in range(tick):
        a = i * iv + statbase
        print '%.2f, '%(dr2ehp(srate(a)*prate(a))/0.8),
        f.write('%.2f, '%(dr2ehp(srate(a)*_prate)/0.8))
    print ''
    f.write('\n')

    print 'brm dm noisb',
    f.write('活tm的(平均收益&急速爆炸), ')
    piv = 1.0/bps(1.5,t3='lb')
    _prate = prate(piv)
    for i in range(tick):
        a = i * iv + statbase
        #print '%.2f, '%(dr2ehp(srate(a)*prate(a))/0.8),
        f.write('%.2f, '%(dr2ehp(srate(a)*_prate)/0.8))
    print ''
    f.write('\n')
   # print 'brm dm 1i1p, ',
   # f.write('1铁1活, ')
   # for i in range(tick):
   #     a = i * iv + statbase
   #     a = a*3.5
   #     print '%.2f, '%(dr2ehp(srate(a)*0.5)/0.8),
   #     f.write('%.2f, '%(dr2ehp(srate(a)*0.5)/0.8))
   # print ''
   # f.write('\n')

    print 'dk,', 
    f.write('骨盾, ')
    for i in range(tick):
        s = i * iv + statbase
        print '%.2f, '%(dr2ehp(dkrate(s))),
        f.write('%.2f, '%(dr2ehp(dkrate(s))))
    print ''
    f.write('\n')




    f.close()


if __name__ == '__main__':
    main()


