numlist = list()

while True :
    inp = input('Enter a number: ,\n or Enter "done" to end the list ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

'''oppure:
total = 0
count = 0
while True :
    inp = input('Enter a number: ,\n or Enter "done" to end the list ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total/count
print('Average: ', average)