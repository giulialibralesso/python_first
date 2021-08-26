counts = dict()
names = ['Anna', 'Alice', 'Franco', 'Berto', 'Lucia', 'Elisa', 'Lucia', 'Berto']
for name in names #[:5] :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

'''oppure:
counts = dict()
names = ['Anna', 'Alice', 'Franco', 'Berto', 'Lucia', 'Elisa', 'Lucia', 'Berto']
 for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)'''