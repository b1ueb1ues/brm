#!/usr/bin/python27
# -*- encoding:utf8 -*-

selfh = 0
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
    crithrate = (crit/400.0 + critbase)/100.0 * 0.65 + 1
    critselfhrate = ((crit/400.0 + critbase)/100.0 + 1) * ((crit/400.0 +critbase )/100.0*0.65 +1)
    versselfhrate = vers/475.0/100.0 + 1
    versavoidrate = vers/950.0/100.0
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
    return ehr

def test1():
    total = 14000
    vers = 0
    crit = 0
    offset = 400
    crit = 0 - offset

   # a = shr(0,0)
   # b = shr(400,0)
   # c = shr(0,400)
   # print a,b,c
   # return

    while(1):
        crit += offset
        if crit > total:
            break
        vers = total - crit
        ret = shr(crit,vers)
        ret2 = ehr(crit,vers)
        print crit,ret,ret2




def main():
    test1()


if __name__ == '__main__':
    main()
