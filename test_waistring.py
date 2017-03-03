from brm import *

'''
a = brm(haste=1.25,palmcdr=1.4,iduration=8.5,equip=['4t','ring','waist'],talent=['black','ht15'],mastery = 0.3)
b = brm(haste=1.25,palmcdr=1.4,iduration=8.5,equip=['4t','ring','waist'],talent=['light','ht15'],mastery = 0.3)
a.run(100000)
b.run(100000)
ar = float(a.getmavoid())
br = float(b.getmavoid())
print 1.0-(1.0-ar)/(1.0-br)
print ar
a.showavoid()
b.showavoid()

exit()
'''

def test2():
    offset = 0.02
    i = 1.1 - offset
    print 'haste\td      \twr       \tno wr    \t'
    while(1):
        if i > 1.4 :
            break
        i += offset
        a = brm(haste=i,palmcdr=1.4,iduration=8.5,equip=['4t','ring','waist'],talent=['black','ht15'],mastery = 0.27, crit = 0.25)
        b = brm(haste=i,palmcdr=1.4,iduration=8.5,equip=['4t'],talent=['black','ht15'],mastery = 0.27, crit = 0.25)
        a.run(100000)
        b.run(100000)

        ar = float(a.getmavoid())
        br = float(b.getmavoid())

        print "%2d%%\t"%((i-1)*100),
        print '%.3f\t'%(1-(1.0-ar)/(1.0-br)),


        print '%s\t'%(a.getmavoid()),
        print '%s\t'%(b.getmavoid()),
        print ' '

test2()
exit()


offset = 0.01
i = 1.0 - offset
print 'haste\telus d(13.3%)\telus d(20.0%)\tblackout combo\thigh tol(10%)\thigh tol(15%)'
while(1):
    if i > 1.5 :
        break
    i += offset
    a = brm(haste=i,equip=['waist','ring'],talent=['black','ed13'],mastery = 0.3)
    b = brm(haste=i,equip=['waist','ring'],talent=['black','ed20'],mastery = 0.3)
    c = brm(haste=i,equip=['waist','ring'],talent=['black','bc'],mastery = 0.3)
    d = brm(haste=i,equip=['waist','ring'],talent=['black','ht'],mastery = 0.3)
    e = brm(haste=i,equip=['waist','ring'],talent=['black','ht15'],mastery = 0.3)
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

offset = 0.01
i = 1.0 - offset
print 'haste\telus d(13.3%)\telus d(20.0%)\tblackout combo\thigh tol(10%)\thigh tol(15%)'
while(1):
    if i > 1.5 :
        break
    i += offset
    a = brm(haste=i,equip=['waist','ring'],talent=['black','ed13'],mastery = 0.3)
    b = brm(haste=i,equip=['waist','ring'],talent=['black','ed20'],mastery = 0.3)
    c = brm(haste=i,equip=['waist','ring'],talent=['black','bc'],mastery = 0.3)
    d = brm(haste=i,equip=['waist','ring'],talent=['black','ht'],mastery = 0.3)
    e = brm(haste=i,equip=['waist','ring'],talent=['black','ht15'],mastery = 0.3)
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

