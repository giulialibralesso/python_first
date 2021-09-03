name = input('Enter a file:')
handle = open(name)

wantedstring = 'hello you'

def detect (string, name) :
    if string in name :
        return True
    else :
        return False

print(detect(wantedstring, name))