import requests,bs4

page=requests.get('http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html')
soup=bs4.BeautifulSoup(page.content,'html.parser')

bycls=soup.find_all('p',class_='outer-text',)
print(bycls[0])
