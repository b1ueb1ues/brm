stagger = 0
iv = 10
puried = 0
staggerin = 0
for i in range(600):
    staggerin += 100
    stagger += 100
    stagger -= stagger * 0.1
    if i % iv >= 0 and i % iv < 1:
        print i,'puried'
        puried += stagger * 0.5
        stagger -= stagger * 0.5
print puried / staggerin


