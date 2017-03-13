#!/usr/bin/python2.7
from statcmp import *

m = 15000.0
h = 0.0
while(1):
    b = brm(equip=[''], mastery = m/40000+0.08, haste = 1 + h/37500)
    b.run(100000)

    print 'mastery: %.1f'%(m/400+8),'haste: %.1f'%(h/375),'|',b.getmavoid()
    m -= 400
    h += 400
    if m <= 400 :
        break
