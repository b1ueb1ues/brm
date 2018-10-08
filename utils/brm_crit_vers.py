#!/usr/bin/python27
# -*- encoding:utf8 -*-


crit2percent = 72.0
vers2percent = 85.0

selfh = 20.0
dmg = 100.0

outerh = 0
dmgtaken = 0
crit = 0
vers = 0

crithrate = 0
critselfhrate = 0
versselfhrate = 0
versavoidrate = 0
critbase = 10

def init(crit,vers):
    global critbase
    crithrate = (crit/crit2percent + critbase)/100.0 * 0.65 + 1
    critselfhrate = ((crit/crit2percent + critbase)/100.0 + 1) * ((crit/crit2percent +critbase )/100.0*0.65 +1)
    versselfhrate = vers/vers2percent/100.0 + 1
    versavoidrate = vers/vers2percent/2/100.0
    return crithrate,critselfhrate,versselfhrate,versavoidrate

def shr(crit,vers):
    global dmg
    crithrate, critselfhrate,versselfhrate,versavoidrate = init(crit,vers)
    dmgtaken =  (dmg-dmg*versavoidrate)
    shr = dmgtaken/versselfhrate/critselfhrate
    return shr

def ehr(crit,vers):
    global dmg
    global sefh
    crithrate, critselfhrate,versselfhrate,versavoidrate = init(crit,vers)
    dmgtaken =  (dmg-dmg*versavoidrate)
    ehr = (dmgtaken - selfh * versselfhrate * critselfhrate)/crithrate
    if 0:
        print selfh, versselfhrate, critselfhrate, crithrate
        print ehr
        if ehr<60:
            exit()
    return ehr

def test1():
    f = open("figure_cv.csv","w")
    f1 = open("figure_all.csv","a")
    total = 3000

   # a = shr(0,0)
   # b = shr(400,0)
   # c = shr(0,400)
   # print a,b,c
   # return

    f.write("crit %.1f,"%(selfh/100))
    f1.write("crit %.1f,"%(selfh/100))
    vers = 0
    crit = 0
    offset = 100
    crit = 0 - offset
    old_r = 0
    while(1):
        crit += offset
        if crit > total:
            break
        vers = total - crit
        vers = 0
        ret = shr(crit,vers)
        ret2 = ehr(crit,vers)
        if old_r == 0:
            old_r = ret2
            continue
        dr = 1.0-ret2/old_r
        old_r = ret2
        f.write("%.4f,"%dr)
        f1.write("%.4f,"%dr)
        print crit,ret,ret2
    f.write('\n')
    f1.write('\n')

    f.write("vers %.1f,"%(selfh/100))
    f1.write("vers %.1f,"%(selfh/100))
    vers = 0
    crit = 0
    offset = 100
    vers = 0 - offset
    old_r = 0
    while(1):
        vers += offset
        if vers > total:
            break
        crit = total - vers
        crit = 0
        ret = shr(crit,vers)
        ret2 = ehr(crit,vers)
        if old_r == 0:
            old_r = ret2
            continue
        dr = 1.0-ret2/old_r
        old_r = ret2
        f.write("%.4f,"%dr)
        f1.write("%.4f,"%dr)
        print vers,ret,ret2
    f.write("\n")
    f1.write("\n")




def main():
    global selfh
    test1()
    selfh = 30.0
    test1()


if __name__ == '__main__':
    main()
