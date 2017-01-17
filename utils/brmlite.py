#!/usr/bin/python2.7
# encoding:utf8
import brm_bps
import random

def testhaste(brm,offset=0.05, ironduration = 9):
	bps=0
	pps=0
	old = 0.01
	i = 1-offset
	while(1):
		if i > 2:
			break
		i+=offset
		bps = brm_bps.bps(haste=i)
		pps = bps - 1.0/ ironduration
		
		print i,'\t',

		a = testinterval(brm,1/pps)
		print 1.0/((1.0-a)/(1.0-old))
		old = a

def testinterval(brm,interval):
	a = 0
	i = interval
	brm.clean()
	for j in range(int(100000/i)):
		brm.iron(i)
		brm.pury()
	a = brm.getavoid()
	return a

def testtalent(ironduration = 8):
	brm = brmlite(t7='ht',waist=1,ring=1)
	brm2 = brmlite(t7='ht',waist=1,ring=1)
	offset = 0.05
	i = 1 - offset
        olda = 0
        oldb = 0
	while(1):
		if i > 2:
			break
		i+=offset
		bps = brm_bps.bps(haste=i,t7='ht',p=1.3)
		pps = bps - 1.0/ ironduration
		bps2 = brm_bps.bps(haste=i,t7 = 'ht',p=2.3)
		pps2 = bps2 - 1.0/ ironduration

		print i,'\t',
		a = testinterval(brm,1/pps)

		print a, 1-(1-a)/(1-olda),
                olda = a
		b = testinterval(brm2,1/pps2)
		print b, 1-(1-b)/(1-oldb)
                oldb = b


	return 0;




def bc(brm):
	for i in range(10):
		brm.lock(3)
		brm.iron(6)
		brm.lock(3)
		brm.pury()
		brm.iron(6)

def p16(brm):	
	for i in range(10000):
		brm.iron(16)
		brm.pury()
	#brm.showavoid()

def ip11(brm):
	for i in range(15):
		brm.face(3)
		brm.iron(9)
		brm.pury()

def plainpury(brm):
	for i in range(30):
		brm.face(6)
		brm.pury()

def hhh(brm):
	for i in range(30):
		brm.iron(5)
		brm.pury()

def art():
	offset = 0.05
	i = 1-offset
	iv = []
	print '\nhaste\tbps\tpuryps\tiron3puryps'
	while(1):
		if i >= 2:
			break
		i+=offset
		a = brm_bps.bps(i,'ht',p=2.3,t3='black')
		b = 1/(a-1.0/7.5)
		c = 1/(a-1.0/9)
		iv.append(int(c))
		print '%.3f\t%.3f\t%.3f\t%.3f'%(i,a,b,c)

def main():
	testtalent()
	return
	brm = brmlite()
	testhaste(brm,offset = 0.01)
	return



	print '2:1 --',
	iv = 1.5
	m = 0.3
	base = 0.8
	brm = brmlite(t7 = 'ht', dodgebase = base, mastery=m, waist = 1, wrist=1, hitiv=iv)
	p16(brm) 
	a = brm.showavoid()

	brm = brmlite(t7 = 'ht', dodgebase = base, mastery=m, waist = 1, hitiv=iv)
	p16(brm)
	b = brm.showavoid()
	print 1-(1-a)/(1-b)
	exit()




	print '2:1 --',
	brm = brmlite(t7 = 'ht')
	p16(brm)
	brm.showavoid()
	f.write('\n')

	print '1:1 --',
	brm = brmlite(t7 = 'ed')
	ip11(brm)
	brm.showavoid()
	f.write('\n')
	
	print '0:1 --',
	brm = brmlite(t7 = 'ed')
	plainpury(brm)
	brm.showavoid()
	f.write('\n')
	
	print 'bc'
	brm = brmlite(t7 = 'bc')
	bc(brm)
	brm.showavoid()
	f.write('\n')

	exit()

	print '\nhigh tolerance'
	brm = brmlite(ht=1)
	p16(brm)
	base = brm.getavoid()

	brm = brmlite(ht=1,ring=1)
	p16(brm)
	ring = brm.getavoid()
	print 'ring:',1-(1-ring)/(1-base)

	brm = brmlite(ht=1,waist=1)
	p16(brm)
	waist = brm.getavoid()
	print 'waist',1-(1-waist)/(1-base)

	brm = brmlite(ht=1,ring=1,waist=1)
	p16(brm)
	ringwaist = brm.getavoid()
	print 'ring+waist',1-(1-ringwaist)/(1-base)

	print '\nelusive dance'

	brm = brmlite(ed=1)
	p16(brm)
	base = brm.getavoid()

	brm = brmlite(ed=1,ring=1)
	p16(brm)
	ring = brm.getavoid()
	print 'ring:',1-(1-ring)/(1-base)

	brm = brmlite(ed=1,waist=1)
	p16(brm)
	waist = brm.getavoid()
	print 'waist',1-(1-waist)/(1-base)



	brm = brmlite(ed=1,ring=1,waist=1)
	p16(brm)
	ringwaist = brm.getavoid()
	print 'ring+waist',1-(1-ringwaist)/(1-base)

out = 0
f = 0

class brmlite:
	#ed : elusive dance
	#ht : high tolerance
	#bc : blackout combo


	global out
	global f
	t7 = ''
	ring = 0
	waist = 0
	wrist = 0
	st = 0  # stagger pool
	sttick = 0 # stagger tick
	avoid = 0 # avoidance
	total = 0 # total dmg taken
	prate = 0.5 # purify rate
	phrate = 0  # purify healrate
	srate = 0.4 # stagger rate
	irate = 0.8 # stagger rate (ironskin)
	stdmgrate = 20 # stagger dmg per sec
	f = 0
	hitiv = 1.5
	hitcount = 0
	ivoffset = 0.1
	stiv = 0.5
	stcount = 0
	clock = 0
	dodgebase = 0.08
	mastery = 0.3
	masterycount = 0
	

	def __init__(this,t7='ht',magic = 0,ring=0,waist=0,wrist=0,hitiv = 1.5,dodgebase = 0.08, mastery = 0):
		random.seed()
		this.hitiv = hitiv
		this.mastery = mastery

		this.dodgebase = dodgebase
		if t7 == 'ht':
			this.srate = 0.5
			this.irate = 0.9
		elif t7 == 'ed':
			this.prate = 0.65
		elif t7 != 'bc':
			print '--t7 err'
			exit()
		if ring == 1:
			this.ring =1
			this.stdmgrate = 26
		if waist ==1:
			this.waist =1
			this.phrate = this.prate * 0.25
		if wrist == 1:
			this.wrist =1
		if magic == 1:
			this.srate /= 2
			this.irate /= 2

	def tick(this,rate):
		this.clock += this.ivoffset
		if this.clock/ this.hitiv > this.hitcount :
			this.hitcount += 1
			if this.mastery == 0:
				this.total += 100.0
				this.st += rate * 100
				this.sttick = this.st/this.stdmgrate
			else :
				r = random.random()
				dodge = this.dodgebase + this.mastery* this.masterycount
				if r < dodge:
					this.masterycount = 0
					if this.wrist == 1:
						this.avoid += this.st *0.05
						this.st -= this.st*0.05
					return
				else:
					this.total += 100.0
					this.st += rate * 100
					this.sttick = this.st/this.stdmgrate
					this.masterycount += 1
		if this.clock/ this.stiv > this.stcount :
			this.stcount += 1
			this.st -= this.sttick



	
	#dmg 2 face
	def face(this,time=1):  
		time = int(time / this.ivoffset)
		for i in range(time):
			this.tick(this.srate)
			#this.total += 100.0
			#this.st += this.srate * 100
			#this.st -= this.st/this.stdmgrate
			global out
			global f
			if out == 1:
				dmg = this.st/this.stdmgrate + 100 - this.srate * 100
				f.write("%d,"%dmg)


			#print this.st

	#dmg 2 ironskin
	def iron(this,time = 1):
		time = int(time / this.ivoffset)
		for i in range(time):
			this.tick(this.irate)
			#this.total += 100.0
			#this.st += this.irate * 100
			#this.st -= this.st/this.stdmgrate
			global out
			global f
			if out == 1:
				dmg = this.st/this.stdmgrate + 100 - this.irate * 100
				print dmg 
				f.write("%d,"%dmg)
	# lock 
	def lock(this,time = 3):
		for i in range(time):
			this.total += 100.0
			this.st += this.irate * 100
			global out
			global f
			if out == 1:
				dmg = 100 - this.irate * 100
				f.write("%d,"%dmg)
	
	def pury(this):
		this.avoid += (this.phrate + this.prate) * this.st 
		this.st -= this.prate * this.st
		this.sttick -= this.sttick * this.prate



	def showavoid(this):
		if this.prate == 0.65:
			print 'ed',  
		elif this.srate == 0.5:
			print 'ht',
		else :
			print 'bc',
		if this.ring == 1 :
			print 'ring',
		if this.waist ==1:
			print 'waist',
		print this.avoid/this.total
		return this.avoid/this.total
	def getavoid(this):
		return this.avoid/this.total
	def getehp(this):
		return 1/(1-this.avoid/this.total)
	def clean(this):
		this.st = 0
		this.avoid = 0
		this.total = 0

if __name__ == '__main__' :
	main()

