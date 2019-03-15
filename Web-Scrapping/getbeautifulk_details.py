import bs4

examplefile = open('example.html')
exampleSoup=bs4.BeautifulSoup(examplefile.read())
elems=exampleSoup.select('#author')
type(elems)
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].attrs)

elemsp = exampleSoup.select('p')
print(len(elemsp))
print(elemsp[0].get_text)
print(elemsp[1].get_text)
spanEle = exampleSoup.select('span')[0]
print(spanEle.get('id'))