name = input('Enter a file:')
handle = open(name, 'r')
wantedstring = 'cat'

def detect (string, file_content) :
    for line in file_content :
        if string not in file_content :
            result = False
        else :
            result = True
        return result

print(detect(wantedstring, handle.read()))
handle.close()