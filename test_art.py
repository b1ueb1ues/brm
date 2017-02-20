from brm import *

"""
a = brm(haste=1.20,iduration=7.5,equip=['4t'],talent=['black','ht15'],mastery = 0.25)
b = brm(haste=1.20,iduration=9,equip=['4t'],talent=['black','ht15'],mastery = 0.25)
c = brm(haste=1.20,iduration=8.5,equip=['4t'],talent=['black','ht15'],mastery = 0.25)
#c = brm(haste=1.25,iduration=8.5,equip=['4t','ring','waist'],talent=[],mastery = 0.3)
a.run(100000)
b.run(100000)
c.run(100000)
ar = float(a.getmavoid())
br = float(b.getmavoid())
cr = float(c.getmavoid())
print ar,br,cr
print 1-(1-ar)*0.88
print 1-(1-br)*0.94
print 1-(1-cr)*0.92
a.showavoid()
b.showavoid()
#c.showavoid()
print 1.0-(1.0-br)/(1.0-ar)
exit()
"""

def test1():
    offset = 0.02
    i = 1.2 - offset
    print 'haste\tironskin      \tbreath'
    while(1):
        if i > 1.4 :
            break
        i += offset
        b = brm(magic = 1,haste=i,palmcdr=1.3,iduration=7.5,equip=['4t'],talent=['black','ht15'],mastery = 0.27)
        a = brm(magic = 1,haste=i,palmcdr=1.3,iduration=9 ,equip=['4t'],talent=['black','ht15'],mastery = 0.27)
        a.run(100000)
        b.run(100000)

        a.showavoid()
        b.showavoid()
        return

        ar = float(a.getmavoid())
        br = float(b.getmavoid())


        print '%.2f\t'%i,
        print '%.4f\t\t'%( 1-(1-ar)*0.88 ),
        print '%.4f\t\t'%(br),
        print ' '

def test2():
    offset = 0.02
    i = 1.1 - offset
    print 'haste\tironskin      \tbreath'
    while(1):
        if i > 1.4 :
            break
        i += offset
        a = brm(magic = 0,haste=i,palmcdr=1.3,iduration=9 ,equip=['4t'],talent=['black','ht15'],mastery = 0.27)
        b = brm(magic = 0,haste=i,palmcdr=1.3,iduration=7.5,equip=['4t'],talent=['black','ht15'],mastery = 0.27)
        a.run(100000)
        b.run(100000)

        ar = float(a.getmavoid())
        br = float(b.getmavoid())


        print '%.2f\t'%i,
        print '%.4f\t\t'%( 1-(1-ar)*0.97 ),
        print '%.4f\t\t'%( 1-(1-br)*0.88 ),
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

