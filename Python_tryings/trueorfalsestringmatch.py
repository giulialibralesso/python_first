name = input('Enter a file:')
handle = open(name, 'r')
wantedstring = 'sun'

def detect (string, file_content) :
    if string not in file_content :
        result = False
    else :
        result = True
    return result

print(detect(wantedstring, handle.read()))
handle.close()