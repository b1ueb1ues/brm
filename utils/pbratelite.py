def prate(iv):
    stagger = 0
    #iv = 10
    puried = 0
    staggerin = 0
    for i in range(600):
        staggerin += 100
        stagger += 100
        stagger -= stagger * 0.1
        if i % iv >= 0 and i % iv < 1:
            puried += stagger * 0.5
            stagger -= stagger * 0.5
    print puried / staggerin


i = 20
while 1:
    i -= 0.5
    if i <= 3:
        break
    print i,
    prate(i)
    print '-------'
    p = prate(4.19)
    p = prate(4.86)


    print '-------'
    bps = 1/4.19
    bps -= 1.0/7
    print 1/bps
    prate(1/bps)

    print '-------'
    bps = 1/4.86
    bps -= 1.0/7
    print 1/bps
    prate(1/bps)
