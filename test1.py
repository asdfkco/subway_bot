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

print(len(result["realtimeArrivalList"]))
for i in range(len(result["realtimeArrivalList"])):
    for j in range(len(result["realtimeArrivalList"][i])):
        print("i:",i)
        print("j:",j)
        if(i!=j and len(result["realtimeArrivalList"])>j):
            if(result["realtimeArrivalList"][i]["trainLineNm"]==result["realtimeArrivalList"][j]["trainLineNm"]):
                print(result["realtimeArrivalList"][i]["trainLineNm"])
                print(result["realtimeArrivalList"][j]["trainLineNm"])
        else:
            break

for i in range(len(result["realtimeArrivalList"])):
    for j in range(len(result["realtimeArrivalList"][i])):
        print("i:",i)
        print("j:",j)
        if(i!=j and len(result["realtimeArrivalList"])>j):
            if(result["realtimeArrivalList"][i]["trainLineNm"]==result["realtimeArrivalList"][j]["trainLineNm"]):
                print(result["realtimeArrivalList"][i]["trainLineNm"])
                print(result["realtimeArrivalList"][j]["trainLineNm"])
        else:
            break
# overlap=[]
# if_overlap = list()
# if1 = 0
# for element in result["realtimeArrivalList"]:
#     if_overlap.append(element["trainLineNm"])
# for i in range(len(if_overlap)):
#     for j in range(i+1):
#         if(i==j):
#             continue
#         else:
#             if(if_overlap[i].replace(" (급행)","")==if_overlap[j].replace(" (급행)","")):
#                 overlap.append(if_overlap[j])
# for element in result["realtimeArrivalList"]:
#     for i in range(len(overlap)):
#         if(element["trainLineNm"]==overlap[i]):
            
    
#배열안에있는것과 같았을때 일단은 저장해두고 나중에 출력하는걸로
# for element in result["realtimeArrivalList"]:
#     print(element["trainLineNm"])
    