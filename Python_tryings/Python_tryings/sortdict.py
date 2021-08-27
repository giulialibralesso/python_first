fname = input('Enter a file: ')
handle = open(fname)
counts = dict()

for line in handle :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

lst = list()
for k, v in counts.items() :
    newtuple = (v, k)
    lst.append(newtuple)
lst = sorted(lst, reverse = True)

#solo le 10 parole più frequenti
for v, k in lst[:10] :
    print(k, v)

#da riga 10 a riga 14 crea dinamicamente una tupla: (v, k) sta per newtuple = (v, k)--> print(sorted([(v, k) for k, v in counts.items()]))

