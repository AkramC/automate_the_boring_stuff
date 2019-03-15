import  requests,bs4
page=requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
#print(page.status_code)
#print(page.content)
soup=bs4.BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
#print(list(soup.children))
html=list(soup.children)[2]
#print(list(html.children))
#print(list(html.children))
#for item in list(html.children):
    #print(item)

body=list(html.children)[3]
pat=list(body.children)[1]
#print(pat.get_text())
p=html.find_all('p')
print(p[0].get_text())
#print(list(html.find_all('p')))