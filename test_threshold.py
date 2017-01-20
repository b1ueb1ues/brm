from brm import *

b = brm(equip=['4t'], haste = 1.25, talent=['ed','black'])
b.run(10000)
print b.blackgain,b.kegcount,b.palmcount,b.brewgain

b = brm(equip=[''], haste = 1.25, talent=['ed','black'])
b.run(10000)
print b.blackgain,b.kegcount,b.palmcount,b.brewgain
exit()

for i in range(10):
    b = brm(equip=[''], haste = 1.0 +0.05* i, talent=['ed','black'])
    b.run(100000)
    #b.showavoid()
#print b.irontimes, b.purytimes, b.blackgain
    print i,100000.0/b.blackgain

