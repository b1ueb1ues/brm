from brm_bps import *

sim_time = 600
isb_boost = 3.5
isb_duration = 7.0
armor_base = 6300.0
stagger_per_agi = 1.4


def foo(x,k):
    return x/(x+k)

def srate(a):
    a = float(a)
    return foo(a, armor_base/stagger_per_agi)

def pdm(iv, a):
    sr = srate(a)
    dt = 0
    staggerin = 0
    puried = 0

    stagger = 0
    for i in range(sim_time):
        dt += 100.0
        staggerin += 100.0 * sr
        stagger += 100.0 * sr
        stagger -= stagger * 0.1
        if i % iv >= 0 and i % iv < 1:
            puried += stagger * 0.5
            stagger -= stagger * 0.5
    print puried / staggerin
    return puried / dt

def ipdm(iv, a):
    if iv >= isb_duration:
        return 0
    iv = 1.0 / (1.0/iv - 1.0/isb_duration)
    a = a * isb_boost
    return pdm(iv, a)

def i1p1dm(iv, a):
    if iv <= isb_duration/2 :
        return 0
    else:
        # 1:1
        iv = iv * 2
        noisb_stin = a/(a+armor_base/stagger_per_agi) * 100
        isb_stin = a/(a+armor_base/stagger_per_agi/isb_boost) * 100
        isb_on = isb_duration
        stagger = 0
        puried = 0
        staggerin = 0
        dt = 0
        for i in range(sim_time):
            dt += 100
            isb_on -= 1
            if isb_on >= 0 :
                staggerin += isb_stin
                stagger += isb_stin
                if isb_on == 0:
                    puried += stagger * 0.5
                    stagger -= stagger * 0.5
            else:
                staggerin += noisb_stin
                stagger += noisb_stin

            stagger -= stagger * 0.1
            if i % iv >= 0 and i % iv < 1:
                    isb_on = isb_duration
        return puried/dt


def fline(f, title, start, stop, iv, callback):
    f.write( '%s'%(title) )
    print '%s'%(title),
    i = start - iv
    while i < stop - iv:
        i += iv
        r = callback(i)
        f.write(',')
        f.write(str(r))
        print ',',
        print str(r),
    print '\n',
    f.write('\n')

def main():
    print pdm(1,50000000000000000)
    exit()


    start = 1
    stop = 1.50
    iv = 0.01
    f = open('pdm.csv','wb')

    fline(f, '', start, stop, iv, lambda x:'')
    fline(f, 'haste', start, stop, iv, lambda x:x)

    agi = 13500
    def foo(x):
        i = 1.0/bps(x)
        return '%.4f'%(1.0/(1.0-pdm(i, agi*1.4)))
    fline(f, 'no_isb %dagi ht '%agi, start, stop, iv, foo)

    agi = 9000
    def foo(x):
        i = 1.0/bps(x)
        return '%.4f'%(1.0/(1.0-pdm(i, agi*1.4)))
    fline(f, 'no_isb %dagi ht '%agi, start, stop, iv, foo)

    agi = 6000
    def foo(x):
        i = 1.0/bps(x)
        return '%.4f'%(1.0/(1.0-pdm(i, agi*1.4)))
    fline(f, 'no_isb %dagi ht '%agi, start, stop, iv, foo)

    agi = 4000
    def foo(x):
        i = 1.0/bps(x)
        return '%.4f'%(1.0/(1.0-pdm(i, agi*1.4)))
    fline(f, 'no_isb %dagi ht '%agi, start, stop, iv, foo)

    agi = 13500
    def foo(x):
        i = 1.0/bps(x)
        return '%.4f'%(1.0/(1.0-ipdm(i, agi*1.4)))
    fline(f, 'keep_isb %dagi ht'%agi, start, stop, iv, foo)

    agi = 9000
    def foo(x):
        i = 1.0/bps(x)
        return '%.4f'%(1.0/(1.0-ipdm(i, agi*1.4)))
    fline(f, 'keep_isb %dagi ht'%agi, start, stop, iv, foo)

    agi = 6000
    def foo(x):
        i = 1.0/bps(x)
        return '%.4f'%(1.0/(1.0-ipdm(i, agi*1.4)))
    fline(f, 'keep_isb %dagi ht'%agi, start, stop, iv, foo)

    agi = 4000
    def foo(x):
        i = 1.0/bps(x)
        return '%.4f'%(1.0/(1.0-ipdm(i, agi*1.4)))
    fline(f, 'keep_isb %dagi ht'%agi, start, stop, iv, foo)




def test_no_palm():
    a = bps(1.3 , t7='ed', t3='bob')
    b = bps(1.3 , t7='ed', t3='bob', p=0)

    pps_a = a - 1.0/7
    pps_b = b - 1.0/7
    pr_a = prate(1/pps_a)
    pr_b = prate(1/pps_b)

    pps_c = a
    pps_d = b
    pr_c = prate(1/pps_c)
    pr_d = prate(1/pps_d)

    dm_a = 0.8 * pr_a
    dm_b = 0.8 * pr_b

    dm_c = 0.5 * pr_c
    dm_d = 0.5 * pr_d
    
    i = 0.3
    print '%.2f'%i, ' brew_cd: %.2f, %.2f '%(1.0/a, 1.0/b)
    print '%.2f'%i, ' pb_interval: %.2f, %.2f '%(1.0/pps_a, 1.0/pps_b)
    print '%.2f'%i, ' pb_interval_noisb: %.2f, %.2f '%(1.0/pps_c, 1.0/pps_d)
    print '| prate_keepisb: %.2f, %.2f \n'\
          '| prate_noisb: %.2f, %.2f \n'\
          '| dm_keepisb: %.2f, %.2f \n'\
          '| dm_noisb: %.2f, %.2f \n'\
              %(
                pr_a, pr_b, pr_c, pr_d,
                dm_a,dm_b,dm_c,dm_d
                )

if __name__ == "__main__":
    main()

