#!/usr/bin/python27
# -*- encoding:utf8 -*-

selfh = 0
dmg = 100.0

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
        outerh = dmgtaken / critselfhrate / vertselfhrate
	return outerh
#	print 'outerhealneeded:',outerh
#	print 'dmgtaken:       ',dmgtaken

f = open("/opt/brm/figure_crt_vers_selfh.csv",'w')
def main():
    global f
    global outerh
    global dmgtaken
    global critselfhrate
    global vertselfhrate
    global crithrate
    global vertavoidrate
    global selfh
    global crit
    global vert

    vert = 0
    crit = 0
    offset = 400
    crit = 0 - offset
    old = 0
    f.write("crit,")
    while(1):
        crit += offset
        if crit > 50 * 400:
            break
        init()
        outerhneeded()
        if old == 0:
            old = outerh
            continue

        print 1-outerh/old
        a = (1-outerh/old)*100
        f.write("%.4f,"%a)
        old = outerh

    print '>>>>>>>>>>'
    f.write('\n')

    vert = 0
    crit = 0
    offset = 400
    vert = 0 - offset
    old = 0
    f.write("vers,")
    while(1):
        vert += offset
        if vert > 50 * 400:
            break
        init()
        outerhneeded()
        if old == 0:
            old = outerh
            continue

        print outerh,
        print 1-outerh/old
        a = (1-outerh/old)*100
        f.write("%.4f,"%a)
        old = outerh



if __name__ == '__main__':
    main()
