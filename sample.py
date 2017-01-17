from brm import *

a = brm(haste = 1.3, equip=[''], mastery = 0.3, meleetakeiv = 1.5)
a.run(100000)
atake = 1-a.showavoid()
print 'brew %d + 3*%d'%(a.brewgot, a.blackgot)

print '------'

b = brm(haste = 1.3, equip=['wrist','waist'], mastery = 0.3, meleetakeiv = 1.5)
b.run(100000)
btake = 1-b.showavoid()
print 'brew %d + 3*%d'%(b.brewgot, b.blackgot)


print '------'
avoid = 1-btake/atake
print 'wrist+waist = ',avoid


