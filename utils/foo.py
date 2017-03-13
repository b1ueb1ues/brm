st = 0.0
purified = 0.0
puryiv = 10
puryrate = 0.5
strate = 0.95
for i in range(100):
    if i % puryiv == 0 :
        purified += st*puryrate
        st -= st * puryrate
    st += strate * 100
    st -= st/10

print purified
base = purified


st = 0.0
purified = 0.0
for i in range(100):
    if i % puryiv == 0 :
        purified += st*puryrate
        st -= st * puryrate
    st += strate * 100
    st -= st/13

print purified
print float(purified)/base
