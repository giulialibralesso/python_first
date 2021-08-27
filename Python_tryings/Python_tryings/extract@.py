import re
line = 'From gianni.rossi@cool.institute.uk'
y = re.findall('^From .*@([^ ]*)', line)
print(y)