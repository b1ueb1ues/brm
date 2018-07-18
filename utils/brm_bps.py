
def bps(haste=1,t7='ht',p=1,t3='bob'):
	brewcd = 14
	bobcd = 120
	ret = 0
	if t3 == 'lb':
		brewcd = brewcd - 3
	if t7 == 'bc' :
		brewcd /= haste
		fivekegtime = 40.0/haste
		brewhaste = (fivekegtime + 30 + 8*p)/fivekegtime
		#print 'brewhaste',brewhaste
		brewcd /= brewhaste
		bobcd /= brewhaste
	elif t7 == 'ht1' or t7 == 'ht' or t7 == 'ht10' :
		haste = haste*1.1
		brewcd /= haste
		fivekegtime = 40.0/haste
		brewhaste = (fivekegtime + 20 + 8*p)/fivekegtime
		brewcd /= brewhaste
		bobcd /= brewhaste
	elif t7 == 'ht15' :
		haste = haste*1.15
		brewcd /= haste
		fivekegtime = 40.0/haste
		brewhaste = (fivekegtime + 20 + 8*p)/fivekegtime
		brewcd /= brewhaste
		bobcd /= brewhaste
	elif t7 == 'ed':
		brewcd /= haste
		fivekegtime = 40.0/haste
		brewhaste = (fivekegtime + 20 + 8*p)/fivekegtime
		brewcd /= brewhaste
		bobcd /= brewhaste
	else :
		print "t7 err"
		return 0;

	if t3 == 'bob' :
		#print 'cd',brewcd,bobcd
		ret = 1.0/brewcd + 2.5/bobcd
	else :
		ret = 1.0/brewcd
	return ret

def pps(haste=1,t7='ht',p=1,t3='bob'):
    return bps(haste,t7,p,t3) - 1.0/6
    


if __name__ == '__main__':
    if 0:
        i = 1.5
        a = bps(i,p=2.3,t3='',t7='ed')
        print 1/a
        exit()

        b = bps(i,p=2.6,t3='bob')
        print a  * 60
        print b * 60
        exit()

    print 'haste bob lb htbob htlb'
    i=1-0.01
    while(1):
        if i >= 1.5:
                break
        i+=0.01
        a = bps(i , t7='ed'   , t3='bob')
        b = bps(i , t7='ed'   , t3='lb')
        c = bps(i , t7='ed'   , t3='lb', p=0)
        #c = bps(i , t7='ht15' , t3='bob')
        #d = bps(i , t7='ht15' , t3='lb')
        print '%.2f'%i,'%.2f, %.2f, %.2f'%(1.0/a, 1.0/b, 1.0/c)
        #b = 1/(a-0.125)
        #c = 1/(a-1.0/9)
        #print i,a,b,clb
    exit()

    a = bps(i,'ht1',p=1.3,t3='bob')
    pps = a - 1.0/8
    print pps
    print 1/pps, a

    print (32.0+15)/(60*3+49)
    print (60*3+49.0)/15
    #	print i,a,
    #	c = bps(i*1.10,'ht',p=2.3,t3='light')
    #	print c,
    #	d = bps(i*1.15,'ht',p=2.3,t3='null')
    #	print d,
    #
    #	b = bps(i,'bc',p=2.3,t3='bob')
    #	print b
    #
    #
    #
