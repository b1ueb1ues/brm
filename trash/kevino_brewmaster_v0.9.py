#!/usr/bin/python27
#---encoding:utf8---

import random
import sys
import getopt
#param
 
talent = 1 # 100 level talent 1~left 2~middle 3~right
t19 = 0 
haste = 20
mastery = 20
arm = 2500
magic_flag = 0 # a flag to judge wether the damage is magic
waist = 0 # the legendery waist that make * brew heal you with 0.25 of the damge it *
ring = 0 # the legendery ring that let * in 13 seconds rather than 10
spell = 10 # the enmey spell that cause huge damage, 10 means the damage is equal to 10 normal attack
spell_cd = 30

'''
def show_help():
	print "How to use brewmaster.py"
	print "Default values:"
	print "talent use *, do not have t19, waist, ring; the haste and mastery is 20%"
	print "the spell damage of enemy is queal to 10 nomarl attack, and the cd is 30s"
	print "use -ta to set talent"
	print "use -t to set t19, use -ha to set haste, use -m to set mastery, use -a to set arms"
	print "use -mf to set the damage is magic or not, use -w and -r to set wether have waist and ring"
	print "use -s to set the damage of enemy spell, use -sc to set the spell cd"
	print "use -help to show this"
	print "Example:"
	print "./python brewmaster.py -ta 1 -t 0 -ha 20 -m 20 -a 2500 -mf 0 -w 0 -r 0 -s 10 -sc 30"

opts, args = getopt.getopt(sys.argv[1:], "ta:t:ha:m:a:mf:w:r:s:sc:h:")

for o,a in opts:
	if o in ("-ta"):
		if a == '1':
			talent = 1
		elif a == '2':
			talent = 2
		elif a == '3':
			talent = 3
		else :
			talent = talent
	if o in ("-t"):
		t19 = a
	if o in ("-ha"):
		haste = int(a)
	if o in ("-m"):
		mastery = int(a)
	if o in ("-a"):
		arm = int(a)
	if o in ("-mf"):
		magic_flag = int(a)
	if o in ("-w"):
		waist = int(a)
	if o in ("-r"):
		ring = int(a)
	if o in ("-s"):
		spell = int(a)
	if o in ("-sc"):
		spell_cd = int(a)
	if o in ("-h"):
		show_help()
'''

# the actual cd of pur_brew to deal with nomarl attack,
# input is the haste and the out put is the cd*2 
def brew_cd(haste):
	#global spell_cd
	brew_basic_cd = 21
	tong_basic_cd = 8
	
	brew_show_cd = brew_basic_cd/(1+haste)
	tong_show_cd = tong_basic_cd/(1+haste)

	if talent == 2 :
		if t19 == 1 :
			tong_cdr = (tong_show_cd*5+8*2.3+5*6)/(tong_show_cd*5)
		else :
			tong_cdr = (tong_show_cd*5+8*1.3+5*6)/(tong_show_cd*5)
	elif t19 == 1 :
		tong_cdr = (tong_show_cd*5+8*2.3+5*4)/(tong_show_cd*5)
	else :
		tong_cdr = (tong_show_cd*5+8*1.3+5*4)/(tong_show_cd*5)

	brew_cd_1 = brew_show_cd/tong_cdr

	ox_cd_1 = 30/tong_cdr
	
	brew_cd_2 = brew_cd_1*ox_cd_1/(brew_cd_1+ox_cd_1)

	case_tiegu = 1/brew_cd_2 - 	0.125
	case_spell = case_tiegu - 1/spell_cd

	brew_cd_actual = 1/case_spell
	brew_cd_result = int(brew_cd_actual*2)+1	

	return brew_cd_result

# to judge wether a nomarl attack is miss
def dodge(mastery):
	global dodge_actual,dodge_count
	flag = random.randint(1,100)
	if flag <= dodge_actual :
		damage = 0
		if talent == 1 :
			dodge_actual = 18
		else :
			dodge_actual = 8
		dodge_count += 1
	else :
		damage = 100
		dodge_actual += mastery
	return damage

# the stagger pool, the out put is the damage of stagger in 0.5s
def pool():
	global stagger_pool
	stagger = 0
	if ring == 1 :
		stagger = stagger_pool/26
	else :
		stagger = stagger_pool/20
	stagger_pool = stagger_pool - stagger
	return stagger

# nomarl attck and the spell, the return is the direct damage
def attack(mastery):
	global attack_count,damage_total,stagger_pool
	damage_add = 0
	direct_damage = 0
	if time % attack_speed == 0 :
		attack_count += 1
		damage_add = dodge(mastery)
		damage_total += damage_add
		stagger_pool += damage_add*stagger_percent
		direct_damage += damage_add*(1-stagger_percent)
	if time != 0 :
		if time % spell_cd == 0:
			damage_add = spell_damage
			damage_total  += damage_add
			stagger_pool += damage_add*stagger_percent
			direct_damage += damage_add*(1-stagger_percent)

	return direct_damage

# calc the effect of pur_brew
def pur_brew():
	global stagger_pool
	pur_effect = 0
	if talent == 1 :
		pur_effect = stagger_pool*0.65
	else :
		pur_effect = stagger_pool*0.5
	stagger_pool = stagger_pool - pur_effect
	if waist == 1 :
		pur_effect += waist_heal(pur_effect)
	return pur_effect

# calc the heal from the waist
def waist_heal(pur_effect):
	heal = 0
	heal = 	pur_effect*0.25
	return heal

# let the battle begin
def battle(mastery):
	global time 
	total_stagger_damage = 0
	total_direct_damage = 0
	basic_direct_damage = 0
	brew_effect = 0
	total_pur_effect = 0
	basic_pur_effect = 0
	basic_stagger_damage = 0
	while time <= total_time :
		basic_direct_damage = attack(mastery)
		total_direct_damage += basic_direct_damage
		if time != 0 :
			basic_stagger_damage = pool()
			total_stagger_damage += basic_stagger_damage
		if time != 0 :
			if time % cd == 0 :
				#print "%f"%stagger_pool
				basic_pur_effect = pur_brew()
				#print "%f"%stagger_pool
				#print "%f"%basic_pur_effect
				total_pur_effect += basic_pur_effect
		if time != 0 :
			if time % spell_cd == 0 :
				basic_pur_effect = pur_brew()
				total_pur_effect += basic_pur_effect
		time += 1
		#print "%f"%stagger_pool

	brew_effect = total_pur_effect/damage_total*100
	dodge_effect = float(dodge_count)/float(attack_count)*100

	print "----------------------------"
	print "brew effect :"+"%f"%brew_effect+"%"
	print "dodge & mastery effect :"+"%f"%dodge_effect+"%"
	brew_dodge = 100 - (100 - brew_effect)/100*(100 - dodge_effect)/100*100
	arm_effect = 1 - float(arm)/float(arm + 7500)
	if talent == 2 :
		allcount = 100 - (100 - brew_dodge)*0.8*arm_effect
	else :
		allcount = 100 - (100 - brew_dodge)*0.95*arm_effect
	print "brew, dodge & mastery effect :"+"%f"%brew_dodge+"%"
	print "brew, dodge, fire, arms & mastery effect :"+"%f"%allcount+"%"
	return 0

damage = 100
dodge_actual = 8
damage_total = 0
stagger_pool = 0
if talent == 3 :
	stagger_percent = 0.9
else :
	stagger_percent = 0.8
if t19 == 1 :
	stagger_percent += 0.05
if magic_flag == 1 :
	stagger_percent /= 2
attack_speed = 3
time = 0
total_time = 20000
haste = float(haste)/100
if talent == 3 :
	cd = brew_cd(haste+0.1)
else :
	cd = brew_cd(haste)
#print "%d"%cd
dodge_count = 0
total_stagger_damage = 0
direct_damage = 0
attack_count = 0
spell_damage = spell*damage

battle(mastery)
