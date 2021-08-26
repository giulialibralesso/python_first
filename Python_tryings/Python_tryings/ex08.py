fname = input('Enter file: ')
handle = open(fname)

di = dict()
for line in handle :
    line = line.rstrip()
    words = line.split()

    for w in words :
        di[w] = di.get(w,0) + 1

        #print (w, di[w])
        #print(di)

#Now we want to find the most common word
largest = -1
theword = None

for k,v in di.items() :
    print(k,v)
    if v > largest :
        largest = v
        theword = k
print('Done: ', theword, largest)


#-----------------------------------------------------------------------------------------------------------

'''oppure:
    for w in words :
        #if the key is not there, the count is zero
        oldcount = di.get(w,0)
        print(w, ': old', oldcount)
        #if the key is already there, add up one to count
        newcount = oldcount + 1
        di[w] = newcount
        print(w, ': new', newcount)
        print(di)'''

#-----------------------------------------------------------------------------------------------------------

'''oppure:
        if w in di :
            di[w] = di[w] + 1
            #print('Existing')
        else :
            di[w] = 1
            #print('New')
        #print(w, di[w])
        print(di)'''

#-----------------------------------------------------------------------------------------------------------

