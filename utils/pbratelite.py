from brm_bps import *


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

def main():
    f = open('hp_haste.csv','wb')
    hpold = 1
    iv = 0.01
    stop = 1.6
    i = 1 - iv
    while i < stop-iv :
        i += iv
        f.write('%.2f, '%i)
    f.write('\n')
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb')
        pr = prate(1.0/a) * 0.5 
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp

    f.write('\n')
    hpold = 1
    i = 1 - iv
    while i < stop-iv :
        i += iv
        a = bps(i, t3='lb') - 1.0/7
        pr = prate(1.0/a) * 0.8
        hp = 1.0/(1.0-pr)
        print '%.2f: pbcd: %.2f, pbrate: %.2f, hp:%.2f(d=%.4f)'\
                        %(i, 1.0/a, pr, hp, hp-hpold)
        f.write('%f, '%hp)
        hpold = hp

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

