selfh = 20.0
dmg = 100.0
hp = 1000

outerh = 0
dmgtaken = 0
crit = 0
vert = 0

crithrate = 0
critselfhrate = 0
vertselfhrate = 0
vertavoidrate = 0
critbase = 10

def init():
	global crit
	global vert
	global critselfhrate
	global vertselfhrate
	global crithrate
	global vertavoidrate
	crithrate = (crit/400.0 + critbase)/100.0 * 0.65 + 1
	critselfhrate = ((crit/400.0 + critbase)/100.0 + 1) * ((crit/400.0 +critbase )/100.0*0.65 +1)
	vertselfhrate = vert/475.0/100.0 + 1
	vertavoidrate = vert/950.0/100.0

def outerhneeded():
	global outerh
	global dmgtaken
	global critselfhrate
	global vertselfhrate
	global crithrate
	global vertavoidrate
	global selfh
	dmgtaken =  (dmg-dmg*vertavoidrate-selfh*vertselfhrate*critselfhrate)
#	print 'dmgt',dmgtaken
#	print 'dmg',dmg
#	print 'selfh*vertselfhrate*critselfhrate',selfh*vertselfhrate*critselfhrate
	outerh = dmgtaken/crithrate
	return outerh
#	print 'outerhealneeded:',outerh
#	print 'dmgtaken:       ',dmgtaken

crit = 0
vert = 7000
dmg = 100.0
selfh = 20.0
init()
print 'vert dmgtaken'
outerhneeded()
tmp = outerh
tmp2 = dmgtaken
print outerh


vert = 0
crit = 7000
dmg = 100.0
selfh = 20.0
init()
print 'crit dmgtaken'
outerhneeded()
print tmp
print outerh
print 'outerhealneeded   critical/versatility',tmp/outerh
print 'time to live   versatility/critical',dmgtaken/tmp2
print '\n'


crit = 0
total = 12000
print 'total stat',total
while(1):
	crit += 400
	if crit > total:
		break
	vert = total - crit
	dmg = 100.0
	selfh = 20.0
	init()
	print 'crit', crit, 'vers', vert,
	outerhneeded()
	print outerh

crit = 0
oldcrit = 0
print 'near'
while(1):
	if crit > 25000:
		break
	oldcrit = crit
	
	vert = 350
	dmg = 100.0
	selfh = 0.0
	init()
	print '-------\ncritrate,',crit
	verseh = outerhneeded()


	crit += 350
	vert = 0
	init()
	criteh = outerhneeded()
	print 'crit adv ', verseh - criteh

	



