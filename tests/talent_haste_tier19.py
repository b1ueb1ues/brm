from _brmtest import *

offset = 0.01
i = 1.1 - offset
print 'haste\t0t     \t\t2t     \t\t4t'
while(1):
    if i > 1.4 :
        break
    i += offset
    c = brm(haste=i,equip=[],talent=['black','ht15'],mastery = 0.27, iduration = 8)
    a = brm(haste=i,equip=['2t'],talent=['black','ht15'],mastery = 0.27, iduration = 8)
    b = brm(haste=i,equip=['4t'],talent=['black','ht15'],mastery = 0.27, iduration = 8)
    a.run(100000)
    b.run(100000)
    c.run(100000)

    print "%2d%%\t"%((i-1)*100),


    print '%s\t'%(c.getmavoid()),
    print '%s\t'%(a.getmavoid()),
    print '%s\t'%(b.getmavoid()),
    print ' '


