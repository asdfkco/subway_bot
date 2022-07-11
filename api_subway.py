import requests
from bs4 import BeautifulSoup
import json

location = input()
key = "5450736268726c6138306668594453"

url = f"http://swopenAPI.seoul.go.kr/api/subway/{key}/json/realtimeStationArrival/0/5/{location}"

line = {"1001":"1호선","1002":"2호선","1003":"3호선","1004":"4호선","1005":"5호선","1006":"6호선","1007":"7호선","1008":"8호선","1009":"9호선","1075":"분당선","1077":"신분당선","1091":"자기부상선"
        ,"1092":"우이신설선","1163":"경의중앙선","1165":"공항철도","1167":"경춘선"}      

arrivalCode = {""}

response = requests.get(url)
result = json.loads(response.text)
for element in result["realtimeArrivalList"]:
        print(element["subwayId"])
        print(element["trainLineNm"])
        print(element["btrainSttus"])
        print(element["barvlDt"])
        print(element[""])