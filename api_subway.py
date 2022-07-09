# import requests
# from bs4 import BeautifulSoup
#
# location = input()
# key = "5450736268726c6138306668594453"
#
# url = f"http://swopenAPI.seoul.go.kr/api/subway/{key}/xml/realtimeStationArrival/0/5/{location}"
#

import requests

url = 'http://openapi.seoul.go.kr:8088/sample/xml/CardSubwayStatsNew/1/5/20220301'

response = requests.get(url)
print(response.content)