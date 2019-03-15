import re
passwd="March2018"
#passregex=re.compile(r'([A-Za-z0-9@#%^&+-=]{8,})')
#mo=passregex.search(passwd)
#print(mo.group())
flag=0
if len(passwd)<8:
    flag= -1
    print("len")
elif not re.search("[a-z]",passwd):
    flag=-1
    print("lowercase")
elif not re.search("[A-Z]",passwd):
    flag=-1
    print("uppercase")
elif not re.search("[0-9]",passwd):
    flag=-1
    print("number")

if flag == 0:
    print("Valid Password")
else:
    print("Invalid Password")