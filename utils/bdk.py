
def rpps(haste=1.15, target=1):
    if target >= 2:
        bs_iv = 3.5
    else:
        bs_iv = 4.5
    rps,rpps = core(haste,bs_iv,target)
    return rpps

def rps(haste=1.15, target=1):
    if target >= 2:
        bs_iv = 3.5
    else:
        bs_iv = 4.5
    rps,rpps = core(haste,bs_iv,target)
    return rps

def core(haste=1.15, bs_iv=4.5, target=1):
    haste = float(haste) * 1.1
    r_recover = 10.0/haste
    r_ps = 3.0/r_recover

    mr_r_ps = 2.0 / (bs_iv*3)
    hs_r_ps = r_ps - mr_r_ps
    #print '--',1/hs_r_ps

    mr_rp_ps = mr_r_ps * 10
    hs_rp_ps = hs_r_ps * (15+2*target)

    rps = r_ps
    rpps = mr_rp_ps + hs_rp_ps
    return rps,rpps

def main():
    hsps_old = 40.0/rpps(1.0,1)
    for i in range(40):
        h = 1+ i/100.0
        hsps = 40.0/rpps(h,1)
        print h,hsps, hsps_old/hsps
        hsps_old = hsps

    exit()

    print 40/rpps(1.1)
    print 40/rpps(1.2)

    print 40/rpps(1.1,4)
    print 40/rpps(1.2,4)

    print rps(1.0,0)
    print rpps(1.0,0)
    print rpps(1.0,1)
    print rpps(1.0,4)


if __name__ == "__main__":
    main()
