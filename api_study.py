import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?'
params ={'serviceKey' : 'GJOmbUJ/nAt/chudgGszaJVRJiuTcd5tIAjvroy7CzulqoCqsVQMMnIgzkKdexeQkkHQjTwkYRla0Z0oNgFaHQ==','returnType':'xml','numOfRows':'100','pageNo':'1','searchDate':'HOUR','sidoName':'서울','ver':'1.0'}

response = requests.get(url, params=params,verify = False)
print(response.url)
soup = BeautifulSoup(response.text,'html.parser')
ItemList = soup.findAll('item')
for item in ItemList:
    print(item.find('datatime').text)  # line1
    print(item.find('khaiValue'))
    print(item.find('so2value').text)
    print(item.find('covalue').text)
    print(item.find('o3value').text)
    print(item.find('no2value').text)
    print(item.find('pm10value').text)
    print(item.find('pm25value').text)
    print(item.find('sidoName'))
    print(item.find('stationName'))
    print('------------------')