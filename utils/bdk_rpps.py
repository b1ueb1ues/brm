
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



def main():
    if 1:
        #rpps(1)
        print rpps(1.0)
        print rpps(1.1)
        hsps_old = 40.0/rpps(1.0,1)
        for i in range(40):
            h = 1 + i/100.0
            hsps = 40.0/rpps(h,0)
            print hsps, hsps_old/hsps
            hsps_old = hsps

        #rpps(1.4)


if __name__ == '__main__':
        main()
