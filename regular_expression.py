import re
heroRegex =re.compile(r'Batman|Tina|Fred')
mo = heroRegex.search('Batman and Tina and Fred')
print(mo.group())

batmanRegx=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batmanRegx.search('Batmobile lost a wheel')
print(mo.group())

batRegex=re.compile(r'Bat(wo)?man')
mo=batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneReg =re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo=phoneReg.search('My number is 555-4242')
print(mo.group())

batRegex=re.compile((r'Bat(wo)+man'))
mo=batRegex.search('The Adventures of Batwoman')
print(mo.group())

haRegex=re.compile('(Ha){0,3}')
mo=haRegex.search('HaHa')
print(mo.group())

phoneNum=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNum.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

beginwithHello=re.compile(r'^Hello')
mo=beginwithHello.search('Hello world')
print(mo)