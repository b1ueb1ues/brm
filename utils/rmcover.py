
stack = 0
end = []
cover = {0:0, 1:0, 2:0, 3:0, 4:0}
for i in range(600):
    if i % 9 == 0:
        stack += 1
        end += [i+20]
    for j in end:
        if i == j:
            end.pop(end.index(j))
            stack -= 1
    cover[stack] += 1

print cover
    


stack = 0
end = []
cover = {0:0, 1:0, 2:0, 3:0, 4:0}
for i in range(600):
    if i % 9 == 0:
        stack += 1
        if i % 32 == 0:
            end += [i+30]
        else:
            end += [i+20]
    for j in end:
        if i == j:
            end.pop(end.index(j))
            stack -= 1
    cover[stack] += 1

print cover
    

stack = 0
end = {}
cover = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(600):
    if i % 10 == 0:
        stack += 1
        if i % 30 == 0:
            e = i + 30
        else:
            e = i + 20
        if e in end:
            end[e] += 1
        else:
            end[e] = 1
    for j in end:
        if i == j:
            stack -= end[j]
            end.pop(j)
            break
    cover[stack] += 1

print cover
    

