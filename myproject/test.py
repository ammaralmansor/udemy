import re

txt = 'k0aA@by'
reg = "[0-9]*[a-z]*[A-Z]*@*by"

x = re.search(reg, txt)
print(x)