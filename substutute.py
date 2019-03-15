import re
ssn='''This is my ssn 312-223-5754 and this is Raks ssn 532-322-4545'''

ssnregex=re.compile(r'(\d{3})-\d{3}-\d{4}')

sb=ssnregex.sub(r'\1-***-****',ssn)

print(sb)