import re

string="    new word with space"
print(string)
stripreg=re.compile(r'(^\s*|\s*$)')
newstring=stripreg.sub('',string)
print(newstring)