f = open("figure.csv",'w')

C = 1-0.0743

st = 0.0
purified = 0.0
for i in range(80):
    st += 95
    st -= st/10
    if i % 8 == 0 :
        st /= 2
        purified += st
    f.write('%.2f,'%(st/10+5))

f.write('\n')

st = 0.0
purified = 0.0
for i in range(80):
    st += 95*C
    st -= st/10
    if i % 10 == 0 :
        st /= 2
        purified += st
    f.write('%.2f,'%(st/10+5*C))
