import re

def R(patt,txt):
    print(re.match(patt, txt))
    print(re.search(patt, txt))
    print(re.findall(patt, txt))

txt = 'xammar12@gmail.com'
p1="00963938764405"
p3="0938764405"
p2="6093876440"
email = "^[a-z][a-zA-Z0-9]+@[a-z]+.com$"

phone1 = "^00963[0-9]{9} | ^09[0-9]{8}"
phone2 = "^09[0-9]{8}"

l=[(1,2),(3,4),(4,5)]
for i,j in l:
    
    print(i,j)