from brm_bps import *


def srate(a):
    a = float(a)
    return a/(a+6300.0/1.4)

def prate(iv):
    stagger = 0
    #iv = 10
    puried = 0
    staggerin = 0
    for i in range(600):
        staggerin += 100
        stagger += 100
        stagger -= stagger * 0.1
        if i % iv >= 0 and i % iv < 1:
            puried += stagger * 0.5
            stagger -= stagger * 0.5
    return puried / staggerin

def iprate(iv, a):
    if iv <= 3.5:
        print('err')
        exit()
    iv = iv * 2
    noisb_stin = a/(a+6300.0/1.4) * 100
    isb_stin = a/(a+6300.0/1.4/3.5) * 100
    isb_on = 7
    stagger = 0
    puried = 0
    staggerin = 0
    dt = 0
    for i in range(600):
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
                isb_on = 7
    return puried/dt

def main():
    f = open('hp_haste.csv','wb')
    iv = 0.01
    stop = 1.35

    f.write('haste:, ')
    i = 1 - iv
    while i < stop-iv :
        i += iv
        f.write('%.2f, '%i)
    f.write('\n')

    f.write('8000a ht 1:1:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb')
        pr = iprate(1.0/a, 8000*1.4)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')


    f.write('6000a ht 1:1:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb')
        pr = iprate(1.0/a, 6000*1.4)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')


    f.write('6000a ht no isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb')
        pr = prate(1.0/a) * srate(6000*1.4)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('6000a no isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb')
        pr = prate(1.0/a) * srate(6000)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('5000a ht no isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb')
        pr = prate(1.0/a) * srate(5000*1.4)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('5000a no isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb')
        pr = prate(1.0/a) * srate(5000)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('4000a ht no isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb')
        pr = prate(1.0/a) * srate(4000*1.4)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('4000a no isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb')
        pr = prate(1.0/a) * srate(4000)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('6000a ht keep isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb') - 1.0/7
        pr = prate(1.0/a) * srate(6000*1.4*3.5)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f) p/s:%.2f'\
                        %(i, 1.0/a, pr, hp, hp-hpold, pr/0.8)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('6000a keep isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb') - 1.0/7
        pr = prate(1.0/a) * srate(6000*3.5)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f) p/s:%.2f'\
                        %(i, 1.0/a, pr, hp, hp-hpold, pr/0.8)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('5000a ht keep isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb') - 1.0/7
        pr = prate(1.0/a) * srate(5000*1.4*3.5)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f) p/s:%.2f'\
                        %(i, 1.0/a, pr, hp, hp-hpold, pr/0.8)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')


    f.write('5000a keep isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb') - 1.0/7
        pr = prate(1.0/a) * srate(5000*3.5)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f) p/s:%.2f'\
                        %(i, 1.0/a, pr, hp, hp-hpold, pr/0.8)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('4000a ht keep isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb') - 1.0/7
        pr = prate(1.0/a) * srate(4000*1.4*3.5)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f) p/s:%.2f'\
                        %(i, 1.0/a, pr, hp, hp-hpold, pr/0.8)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')

    f.write('4000a keep isb:, ')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb') - 1.0/7
        pr = prate(1.0/a) * srate(4000*3.5)
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f) p/s:%.2f'\
                        %(i, 1.0/a, pr, hp, hp-hpold, pr/0.8)
        f.write('%f, '%hp)
        hpold = hp
    f.write('\n')





    f.write('\n')
    i = 1 - iv
    while i < stop-iv :
        i += iv
        f.write('%.2f, '%i)
    f.write('\n')
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = 1.0/bps(i, t3='lb')
        f.write('%f, '%(a))
    f.write('\n')

    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = 1.0/(bps(i, t3='lb') - 1.0/7)
        f.write('%f, '%a)
    f.write('\n')

    f.close()
    


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

