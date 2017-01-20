#!/usr/bin/python2.7
from brm import *
import brm_magic

c = 15000.0
h = 0.0

selfhrate = 0.15

critrate = 0.1 + c/40000
while(1):
    
    b = brm_magic.brm(equip=[''], haste = 1 + h/37500)
    b.run(100000)

    try:
        btake= 1 - float(b.getmavoid())
    except:
        print b.getmavoid()
        print 'no iron'
        c -= 400
        h += 400
        if c <= 400 :
            break
        continue


    selfh = btake * selfhrate * (critrate + 1) * (critrate*0.65 + 1)
    
    ehrps = (btake - selfh)/(1+ critrate * 0.65)



    print 'crit: %.1f'%(c/400+10),'haste: %.1f'%(h/375),'|',ehrps
    c -= 400
    h += 400
    if c <= 400 :
        break

