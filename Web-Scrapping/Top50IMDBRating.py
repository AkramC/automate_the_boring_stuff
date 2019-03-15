import requests,bs4,re

res=requests.get('http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1')
html_soup=bs4.BeautifulSoup(res.content,'html.parser')
movie_details=html_soup.find_all('div',class_="lister-item mode-advanced")
names=[]
years=[]
imdb_ratings=[]
metascores=[]
directors=[]
votes=[]
for movie in movie_details :
    if movie.find("div",class_="inline-block ratings-metascore") is not None:
        movie_name=movie.h3.a.get_text()
        names.append(movie_name)
        year=movie.find('span',class_="lister-item-year").get_text()
        year=re.sub('\(|\)|I','',year).strip()
        years.append(year)
        imdb_rating=movie.find("div",class_="ratings-bar").strong.get_text()
        imdb_ratings.append(int(imdb_rating))
        metascore=movie.find("div",class_="inline-block ratings-metascore").span.get_text()
        metascores.append(metascore)
        director=movie.find("div",class_="lister-item-content").find_all('p')[2].a.get_text()
        directors.append(director)
        vote=movie.find('p',class_="sort-num_votes-visible").find_all('span')[1].get_text()
        votes.append(int(vote))
