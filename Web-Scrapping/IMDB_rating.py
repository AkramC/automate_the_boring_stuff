import requests,bs4,re

res=requests.get('https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1')
html_soup=bs4.BeautifulSoup(res.text,'html.parser')
movie_details=html_soup.find_all('div',class_="lister-item mode-advanced")
logan=movie_details[0]
print(logan.h3.a.get_text())
year=logan.h3.find('span',class_="lister-item-year text-muted unbold").get_text()
print(re.sub('\(|\)','',year))
rating=float(logan.strong.get_text())
rat=logan.find("div",class_="ratings-bar").strong.get_text()
print(rat)
metascore=logan.find("div",class_="inline-block ratings-metascore").span.get_text()
print(metascore)
director=logan.find('div',class_="lister-item-content").find_all('p')[2].a.get_text()
print(director)
cast=logan.find('div',class_="lister-item-content").find_all('p')[2].find_all('a')
castnamelist=[star.get_text() for star in cast]
castname=",".join(castnamelist[1:])
print(castname)
votes=logan.find('p',class_="sort-num_votes-visible").find_all('span')[1].get_text()
print(votes)