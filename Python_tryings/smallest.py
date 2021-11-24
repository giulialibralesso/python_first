numbers = [9, 41, 12, 3, 74, 15, 3, 8]
smallest = None
for the_num in numbers :
    if smallest is None :
        smallest = the_num
    elif the_num < smallest :
        smallest = the_num
    print(smallest, the_num)

'''oppure:
numbers = [9, 41, 12, 3, 74, 15, 3, 8]
count = 0
smallest = 0
for number in numbers :
    if count == 0 :
        smallest = number
        count = 1
    elif number < smallest :
        smallest = number
print(smallest)'''
