name = input('Insert a file: ')
handle = open(name)
count = 0

for lines in handle :
    words = lines.split()
    for word in words :
        for chars in word :
            count += 1
print('number of characters: ', count)