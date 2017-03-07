#!/usr/bin/python27
# -*- encoding:utf8 -*-

dodgebase = 0.08 # base dodge+rate
o_dmg_avoid = 0
f = open("/opt/brm/figure_mastery.csv",'w')
def main(mastery):
    global f
    #mastery = 0.10 # mastery
    global o_dmg_avoid

    i = 0
    sum_attack = 0
    chance = 0
    o_chance = 0
    for i in range(12):
        if o_chance >= 1 :
                break

        dodge = dodgebase + mastery*i
        if dodge > 1:
                dodge = 1
        chance = (1 - o_chance) * dodge
        o_chance += chance
        sum_attack += chance * (i + 1)

#print sum_attack
    dodge_avg = 1/sum_attack
    print "dodge average:", dodge_avg

    dmg_avoid = 1 - (1 - dodge_avg) / (1 - dodgebase)

    if o_dmg_avoid == 0:
        o_dmg_avoid = dmg_avoid
        return

    print "attack dmg avoid:", dmg_avoid
    print "attack dmg avoid than before :", 1-(1-dmg_avoid)/(1-o_dmg_avoid)
    a = 1-(1-dmg_avoid)/(1-o_dmg_avoid)
    if o_dmg_avoid != 0 :
        f.write("%.4f,"%(a*100))
    o_dmg_avoid = dmg_avoid 
#	print "equivalent health increaced:", 1/(1-dmg_avoid)

if __name__ == '__main__':
    i = 0.08 - 0.01
    dodgebase = 0.40
    while(1):
        i+=0.01
        print "-----\n mastery = ",i
        main(i)
        if i >= 0.5:
            break;
	
    exit()
#	i = 0
#	dodgebase = 0.10
#	main(0.31)
#	exit()

    i = 0.27
    dodgebase = 0.08
    main(i)
    i = 0.27
    dodgebase = 0.08 +0.27
    main(i)
    exit()

    i = 0
    dodgebase = 0.08
    while(1):
        i+=0.01
        print "-----\n mastery = ",i
        main(i)
        if i >= 0.4:
            break;


