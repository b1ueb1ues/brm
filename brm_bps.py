
def bps(haste=1,t7='ht',p=1.3,t3='black'):
	brewcd = 21
	blackcd = 90
	ret = 0
	if t3 == 'light':
		brewcd = 18
	if t7 == 'bc' :
		brewcd /= haste
		fivekegtime = 40.0/haste
		brewhaste = (fivekegtime + 30 + 8*p)/fivekegtime
		#print 'brewhaste',brewhaste
		brewcd /= brewhaste
		blackcd /= brewhaste
	elif t7 == 'ht1' or t7 == 'ht' or t7 == 'ht10' :
		haste = haste*1.1
		brewcd /= haste
		fivekegtime = 40.0/haste
		brewhaste = (fivekegtime + 20 + 8*p)/fivekegtime
		brewcd /= brewhaste
		blackcd /= brewhaste
	elif t7 == 'ht15' :
		haste = haste*1.15
		brewcd /= haste
		fivekegtime = 40.0/haste
		brewhaste = (fivekegtime + 20 + 8*p)/fivekegtime
		brewcd /= brewhaste
		blackcd /= brewhaste
	elif t7 == 'ed':
		brewcd /= haste
		fivekegtime = 40.0/haste
		brewhaste = (fivekegtime + 20 + 8*p)/fivekegtime
		brewcd /= brewhaste
		blackcd /= brewhaste
	else :
		print "t7 err"
		return 0;

	if t3 == 'black' :
		#print 'cd',brewcd,blackcd
		ret = 1.0/brewcd + 2.5/blackcd
	else :
		ret = 1.0/brewcd
	return ret

if __name__ == '__main__':
	i=1-0.01
	while(1):
		if i >= 1.5:
			break
		i+=0.01
		a = bps(i,'ht',p=1.3,t3='black')
		#b = 1/(a-0.125)
		#c = 1/(a-1.0/9)
		#print i,a,b,c

        a = bps(i,'ht1',p=1.3,t3='black')
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
	#	b = bps(i,'bc',p=2.3,t3='black')
	#	print b
	#
	#
	#
