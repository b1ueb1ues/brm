#!/usr/bin/python2.7
from statcmp import *

m = 16000.0
h = 0.0
while(1):
    b = brm(equip=['wrist','4t'],talent=['black','ed20'], mastery = m/40000+0.08, haste = 1 + h/37500, meleetakeiv = 0.75)
    b.run(100000)
    print 'mastery: %.1f'%(m/400+8),'haste: %.1f'%(h/375),'|',b.getmavoid(),' <<<<<<<<<  '

    m -= 400
    h += 400
    if m <= 400 :
        break
