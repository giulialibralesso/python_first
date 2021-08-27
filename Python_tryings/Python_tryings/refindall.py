import re
x = 'My 2 favorite numbers are 7 and 22'
y = re.findall('[0-9]+', x) #cercherà in x solo cifre comprese tra 0 e 9
print(y)
z = re.findall('[AEIOU]+', x) #cercherà in x solo le vocali in maiuscolo
print(z)