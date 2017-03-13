st = 0.0
pury = 0.0
time = 1000
stin = 0.0

for i in range(1000):
    st += 95
    stin += 95
    st -= st * 0.1
    if i % 10 == 9 :
        tmp = 500
        st += tmp
        stin += tmp
        st -= st * 0.5
        pury += st

print pury/time/100

st = 0.0
pury = 0.0
time = 1000

for i in range(1000):
    st += 95
    st -= st * 0.1
    if i % 10 == 9 :
        st -= st * 0.5
        pury += st
        tmp = 500
        st += tmp
        stin += tmp

print pury/time/100
