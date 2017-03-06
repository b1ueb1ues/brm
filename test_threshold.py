from brm import *

b = brm(equip=['4t'], haste = 1.20, talent=['ht15','black'], mastery=0.27)
b.run(100000)
b.showavoid()
exit()

b = brm(equip=['4t'], haste = 1.07, talent=['ht15','black'])
b.run(100000)
print b.blackgain,b.brewgain,b.brewcdwaste,b.blackcdwaste

b = brm(equip=['4t'], haste = 1.08, talent=['ht15','black'])
b.run(100000)
print b.blackgain,b.brewgain,b.brewcdwaste,b.blackcdwaste

b = brm(equip=['4t'], haste = 1.20, talent=['ht15','black'])
b.run(100000)
print b.blackgain,b.brewgain,b.brewcdwaste,b.blackcdwaste
exit()

for i in range(10):
    b = brm(equip=[''], haste = 1.0 +0.05* i, talent=['ed','black'])
    b.run(100000)
    #b.showavoid()
#print b.irontimes, b.purytimes, b.blackgain
    print i,100000.0/b.blackgain

