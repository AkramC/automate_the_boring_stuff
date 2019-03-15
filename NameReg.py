import re
inputstr='Bob pets cats.'
theregex=re.compile(r'((Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs))')
mo=theregex.search(inputstr)
print(mo.group())