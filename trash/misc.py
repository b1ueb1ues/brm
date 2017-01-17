st = 0
st2 = 0
stt = 0
stt2 = 0

for i in range(20):
    
    print i, st/10,st2/13
    st += 90
    st -= st/10
    st2 += 90
    st2 -= st2/13
    stt += st/10
    stt2 += st2/13

st /= 2
st2 /= 2

for i in range(20):
    st += 90
    st -= st/10
    st2 += 90
    st2 -= st2/13
    stt += st/10
    stt2 += st/13
    print i, st/10,st2/13
        


st /= 2
st2 /= 2

for i in range(20):
    st += 90
    st -= st/10
    st2 += 90
    st2 -= st2/13
    stt += st/10
    stt2 += st/13
    print i, st/10,st2/13

print stt, stt2
