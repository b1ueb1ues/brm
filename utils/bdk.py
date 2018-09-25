
def rpps(haste=1.15,bs_iv=4.5, target=1):
    rps,rpps = core(haste,bs_iv,target)
    return rpps

def rps(haste=1.15,bs_iv=4.5, target=1):
    rps,rpps = core(haste,bs_iv,target)
    return rps

def core(haste=1.15,bs_iv=4.5, target=1):
    haste = float(haste) * 1.1
    r_recover = 10.0/haste
    r_ps = 3.0/r_recover

    mr_r_ps = 2.0 / (bs_iv*3)
    hs_r_ps = r_ps - mr_r_ps
    print '--',1/hs_r_ps

    mr_rp_ps = mr_r_ps * 10
    hs_rp_ps = hs_r_ps * (15+2*target)

    rps = r_ps
    rpps = mr_rp_ps + hs_rp_ps
    return rps,rpps

def main():
    print 40/rpps(1.1)
    print 40/rpps(1.2)

    print 40/rpps(1.1,3.5,4)
    print 40/rpps(1.2,3.5,4)

    print rps(1.0,4.5,0)
    print rpps(1.0,4.5,0)
    print rpps(1.0,4.5,1)
    print rpps(1.0,4.5,4)


if __name__ == "__main__":
    main()
