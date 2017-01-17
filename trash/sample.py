# -*- encoding:utf-8


stg = 0.0
hp = 450
mhp = 450
clock = 0

dmg = 100
hps = 40

print "time\t stagger\t stg/mhp\t hp"
for j in range(5):
    for i in range(12):
        clock += 1
        stg += dmg * 0.8
        hp -= dmg * 0.2
        
        stgps = stg/13
        stg -= stgps

        hp -= stgps
        hp += hps
        if hp > mhp :
            hp = mhp
        print "%d\t %.1f   \t %.1f    \t %.1f\t"%(clock,stg,stg/mhp,hp)
    stg *= 0.5
    print 'purify'








exit()

stagger = 0    #醉拳
damage = 100   #秒伤
purify = 0  #活血掉的值

#醉拳戒指 坚定 被攻击10秒
for i in range(10) :
    stagger +=  damage * 0.9
    stagger -=  stagger / 13

#喝活血
purify += stagger * 0.5
stagger -= stagger * 0.5

#再来一遍
for i in range(10) :
    stagger += damage * 0.9
    stagger -= stagger / 13

#喝活血
purify += stagger * 0.5
stagger -= stagger * 0.5

#输出活血掉的醉拳占醉拳百分比
print purify/(damage * 20 * 0.9)

