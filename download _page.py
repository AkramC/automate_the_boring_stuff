import requests

res= requests.get('https://automatetheboringstuff.com/files/rj.txt')
#type(res)
#res.status_code ==requests.codes.ok
#print(res.text[:250])
res.raise_for_status()
playFile=open('RomeandJuilet.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close() 