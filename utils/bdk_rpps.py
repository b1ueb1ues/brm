
# -*- encoding:utf8
def rpps(haste=1.1,target=1):
    haste = float(haste) * 1.1
    bsiv = 4.5
    if target >= 2:
        bsiv = 3.5
    rcd = 10.0/haste
    rps = 3.0/rcd
    mr_rps = 2.0/(bsiv*3)
    mr_rpps = 10 * mr_rps
    ds_ps = rps - mr_rps
    ds_rps = ds_ps 
    ds_rpps = ds_ps * (15 + 2*target)
    rpps = ds_rpps+mr_rpps
    #print 'mrcd:%.2f, dscd:%.2f, rps:%.2f, rpps:%.2f'%(3.5*3, 1.0/ds_ps, rps, rpps)
    return rpps


def dm(haste,vers,mast):
    dt = 0
    dm = 0
    iv = 40.0/rpps(haste,1)
    iv1 = iv - 1
    for i in range(10000):
        i = i+1
        dt += 100
        if i%iv < 1:
            dm += 500.0 * (vers/2)
            dm += 500.0 * (1-vers/2) * (0.25*1.08) * (1+vers) * (1+mast)
    return dm/dt



def dm4(haste,vers,mast):
    dt = 0
    dm = 0
    iv = 40.0/rpps(haste,4)
    iv1 = iv - 1
    for i in range(10000):
        i = i+1
        dt += 100
        if i%iv < 1:
            dm += 500.0 * (vers/2)
            dm += 500.0 * (1-vers/2) * (0.25*1.08) * (1+vers) * (1+mast)
    return dm/dt


def main():
    if 1:
        #hsps_old = 40.0/rpps(1.0,1)
        print '- h 1t ----------'
        dr_old = dm(1, 0, 0.16)
        for i in range(30):
            i = i*100.0
            h = 1.0 + i/100/68
            dr = dm(h, 0, 0.16)
            print "%.4f, %.4f, %.4f"%(h, dr, 1-(1-dr)/(1-dr_old))
            dr_old = dr

        print '- h vm ----------'
        dr_old = dm(1, 0, 0.16)
        for i in range(30):
            i = i*100.0
            h = 1.0 + i/100/68
            dr = dm(h, 1.2, 0.16)
            print "%.4f, %.4f, %.4f"%(h, dr, 1-(1-dr)/(1-dr_old))
            dr_old = dr

        print '- h 4t ----------'
        dr_old = dm4(1, 0, 0.16)
        for i in range(30):
            i = i*100.0
            h = 1.0 + i/100/68
            dr = dm4(h, 0, 0.16)
            print "%.4f, %.4f, %.4f"%(h, dr, 1-(1-dr)/(1-dr_old))
            dr_old = dr

        print '- m ----------'
        dr_old = dm(1, 0, 0.16)
        for i in range(30):
            i = i*100.0
            m = i/100/72*2 + 0.16
            dr = dm(1, 0, m)
            print "%.4f, %.4f, %.4f"%(m, dr, 1-(1-dr)/(1-dr_old))

        print '- m 1.2h----------'
        dr_old = dm(1, 0, 0.16)
        for i in range(30):
            i = i*100.0
            m = i/100/72*2 + 0.16
            dr = dm(1.2, 0, m)
            print "%.4f, %.4f, %.4f"%(m, dr, 1-(1-dr)/(1-dr_old))

        print '- v ----------'
        dr_old = dm(1, 0, 0.16)
        for i in range(30):
            i = i*100.0
            v = i/100/85
            dr = dm(1, v, 0.16)
            print "%.4f, %.4f, %.4f"%(v, dr, 1-(1-dr)/(1-dr_old))

        print '- v 1.2h----------'
        dr_old = dm(1, 0, 0.16)
        for i in range(30):
            i = i*100.0
            v = i/100/85
            dr = dm(1.2, v, 0.16)
            print "%.4f, %.4f, %.4f"%(v, dr, 1-(1-dr)/(1-dr_old))

        #rpps(1.4)

        dr = dm(1.2, 0.1, 0.16)
        print dr
        dr = dm(1.0, 0.18, 0.35)
        print dr

if __name__ == '__main__':
        main()
