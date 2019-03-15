import requests,webbrowser,bs4,sys

print("Google.......")
res=requests.get('http://google.com/search?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text)
linkEle = soup.select('a')
numOpen= min(5,len(linkEle))

for i in range(numOpen):
    print(linkEle[i])
    #webbrowser.open('http://google.com' + linkEle[i].get('href'))
   # webbrowser.open(linkEle[i].get('href'))