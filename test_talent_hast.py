from brm import *
offset = 0.01
i = 1.0 - offset
print 'haste\telus d(13.3%)\telus d(20.0%)\tblackout combo\thigh tol(10%)\thigh tol(15%)'
while(1):
    if i > 1.5 :
        break
    i += offset
    a = brm(haste=i,equip=[''],talent=['black','ed13'],mastery = 0.2)
    b = brm(haste=i,equip=[''],talent=['black','ed20'],mastery = 0.2)
    c = brm(haste=i,equip=[''],talent=['black','bc'],mastery = 0.2)
    d = brm(haste=i,equip=[''],talent=['black','ht'],mastery = 0.2)
    e = brm(haste=i,equip=[''],talent=['black','ht15'],mastery = 0.2)
    a.run(100000)
    b.run(100000)
    c.run(100000)
    d.run(100000)
    e.run(100000)

    print "%2d%%\t"%((i-1)*100),


    print '%s\t'%(a.getmavoid()),
    print '%s\t'%(b.getmavoid()),
    print '%s\t'%(c.getmavoid()),
    print '%s\t'%(d.getmavoid()),
    print '%s\t'%(e.getmavoid()),
    print ' '


