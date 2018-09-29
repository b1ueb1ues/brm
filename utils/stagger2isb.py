
def s2i(p):
    p = float(p)
    a = p / (1-p) # *c
    isb = a * 3.5
    isbp = isb/(isb+1)
    return isbp

def s2ht(p):
    p = float(p)
    a = p / (1-p) # *c
    isb = a * 1.4
    isbp = isb/(isb+1)
    return isbp

def s2a(p, c=7100):
    p = float(p)
    a = p / (1-p) # *c
    agi = a/1.4 * c
    return agi

for i in range(60):
    i = 0.4 + 0.01*i

    print "%.2f, %.4f, %.4f, %.4f| %.0f, %.0f, %.0f"%(i,s2ht(i),s2i(i),s2i(s2ht(i)), s2a(i,6300),s2a(i,7100),s2a(i,9311.4))

