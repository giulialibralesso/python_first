han = open('mbox-short.txt')

for line in han :
    line = line.rstrip() #deletes white spaces
    wds = line.split()
    #guardian pattern
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])