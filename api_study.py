import json
import requests

location = input()

with open ("./token/token.json", "r") as f:
    token = json.load(f)
    
key = token["key"]

url = f"http://swopenAPI.seoul.go.kr/api/subway/{key}/json/realtimeStationArrival/1/6/{location}"
print(location)
response = requests.get(url)
result = json.loads(response.text)
print(url)

# 포문 한개더 만들어서 위에서 비교 같은거는 리스트에 넣기 밑에서 비교해서 같은거는 따로처리한다
overlap=[]
if_overlap = list()
if1 = 0
for element in result["realtimeArrivalList"]:
    if_overlap.append(element["trainLineNm"])
for i in range(len(if_overlap)):
    for j in range(i+1):
        if(i==j):
            continue
        else:
            if(if_overlap[i].replace(" (급행)","")==if_overlap[j].replace(" (급행)","")):
                overlap.append(if_overlap[j])
for element in result["realtimeArrivalList"]:
    if
#배열안에있는것과 같았을때 일단은 저장해두고 나중에 출력하는걸로
# for element in result["realtimeArrivalList"]:
#     print(element["trainLineNm"])
    