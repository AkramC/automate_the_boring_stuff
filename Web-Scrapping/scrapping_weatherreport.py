import requests,bs4

pag=requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W6xI4WgzbIU')
soup=bs4.BeautifulSoup(pag.content,'html.parser')
forcastdiv=soup.find(id='seven-day-forecast')
#print(forcastdiv)
forcast_items=forcastdiv.find_all(class_="tombstone-container")
tonight=forcast_items[0]
print(tonight.prettify())
period=tonight.find(class_="period-name")
desc=tonight.find(class_="short-desc")
temp=tonight.find(class_="temp temp-low")
print(period.get_text())
print(desc.get_text())
print(temp.get_text())

short_desc=[sd.get_text() for sd in forcastdiv.select(".tombstone-container .short-desc")]

print(short_desc)