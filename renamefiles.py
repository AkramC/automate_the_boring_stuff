import re,shutil,os

pathfile='F:\\program_create'

datereg=re.compile(r'''
^(.*?)
((0|1)\d{1})-
((0|1|2|3)\d)-
((19|20)\d\d)
(.*?)$
''',re.VERBOSE)
for file in os.listdir(pathfile):
    print(file)
    mo=datereg.search(file)
    if(mo == None):
        continue
    beforepart=mo.group(1)
    monthpart=mo.group(2)
    daypart=mo.group(4)
    yearpart=mo.group(6)
    afterpart=mo.group(8)
    europartfilename=beforepart+daypart+'-' +monthpart+'-'+yearpart+afterpart
    print("Euro File name is %s"%(europartfilename) )
    americanfilepath=os.path.join(pathfile,file)
    fullpath=os.path.join(pathfile,europartfilename)
    print(fullpath)
    shutil.move(americanfilepath,fullpath)


