counts = dict()
line = input('Enter a new line of text: ')
words = line.split()

for word in words :
    counts[word] = counts.get(word, 0) + 1
print('Counts: ', counts)
