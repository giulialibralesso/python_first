di = {'a': 10, 'b': 2, 'c': 3}
tmp = list()
for k, v in di.items() :
    tmp.append(v, k)
    tmp = sorted(tmp, reverse = True)
print(tmp)