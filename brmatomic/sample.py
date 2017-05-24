from brm import *

a = brm(haste = 1.3, equip=['4t'], mastery = 0.3, meleetakeiv = 1.5)
a.run(100000)
atake = 1-a.showavoid()
print 'brew %d + 3*%d'%(a.brewgain, a.blackgain)

print '------'

b = brm(haste = 1.3, equip=['4t','wrist','waist'], mastery = 0.3, meleetakeiv = 1.5)
b.run(100000)
btake = 1-b.showavoid()
print 'brew %d + 3*%d'%(b.brewgain, b.blackgain)


print '------'
avoid = 1-btake/atake
print 'wrist+waist = ',avoid


