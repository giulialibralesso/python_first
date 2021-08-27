import re
x = 'From: Using this thing: home'
#cerca una stringa che inizia con "F" ^); (seguito da un qualsiasi numero di caratteri (.); non scegliendo la stringa più lunga (+?); che termina con il carattere ":"
y = re.findall('^F.+?:', x)