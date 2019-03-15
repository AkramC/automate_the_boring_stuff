import requests,bs4,webbrowser,sys

print('Seraching Amazon.....')
res=requests.get('https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='+ 'wireless headphone')
soup=bs4.BeautifulSoup(res.content)
#linkEle=soup.select('::before ')
text = soup.findNext('div',{'class':'class_value'}).findNext('div',{'id':'id_value'}).findAll('a')
#webbrowser.open('https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='+ 'wireless headphone')
for i in range(1):
    print(text[i])