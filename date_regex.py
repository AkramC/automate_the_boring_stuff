import re
date='08-22-2018'

dateregex=re.compile(r'([0-3][0-9]-[0-9]{2}-[0-9]{4}|[0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]{2}-[0-3][0-9]-[0-9]{4})')

mo=dateregex.search(date)
print(mo.group())