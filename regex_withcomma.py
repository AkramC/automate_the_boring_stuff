import  re
#num='1,222,234,567'
num='2,532'

commareg=re.compile('(^((\d{1,3})?)(,\d{3})+$)')
mo=commareg.search(num)
print(mo.group()) 