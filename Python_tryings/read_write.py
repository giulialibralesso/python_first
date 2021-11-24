phrase1 = 'hello you'
phrase2 = 'goodbye you'
name = input('Enter a file: ')

with open(name, 'r') as handle :
    data = handle.read()
    handle.close()

newdata = data.replace(phrase1, phrase2)

with open(name, 'w') as handle :
    handle.write(newdata)
    handle.close()