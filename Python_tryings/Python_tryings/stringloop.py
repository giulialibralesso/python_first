fruit = 'banana'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1

'''oppure:
fruit = 'banana'
for letter in fruit :
    print(letter)
'''

'''oppure, se volessi sapere quante volte trovo una 'a' in 'banana':
fruit = 'banana'
count = 0
for letter in fruit :
    if letter == 'a' :
        count = count + 1
print(count, letter)
'''
