import re
inputstring='''http://google.com
http://facebook.com
https://youtube.com'''

http_regex=re.compile(r'((http[s]?):\/\/[a-zA-Z0-9.]+)',re.VERBOSE)

for wb in http_regex.findall(inputstring):
    print(wb)