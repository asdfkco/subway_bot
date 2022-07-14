import requests
import json
import math



location = input()

with open ("./token/token.json", "r") as f:
    token = json.load(f)
    
key = token["key"]

url = f"http://swopenAPI.seoul.go.kr/api/subway/{key}/json/realtimeStationArrival/0/8/{location}"

line = {"1001":"1호선","1002":"2호선","1003":"3호선","1004":"4호선","1005":"5호선","1006":"6호선","1007":"7호선","1008":"8호선","1009":"9호선","1075":"분당선","1077":"신분당선","1091":"자기부상선"
        ,"1092":"우이신설선","1163":"경의중앙선","1165":"공항철도","1167":"경춘선"}      

arrivalCode = {"0":"진입", "1":"도착", "2":"출발", "3":"전역출발", "4":"전역진입", "5":"전역도착", "99":"운행중"}

img = {"1호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846742421541077/unknown.png",
       "2호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846742652231790/unknown.png",
       "3호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846742832590999/unknown.png",
       "4호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846743071657984/unknown.png",
       "5호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846743264600114/unknown.png",
       "6호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846743457546280/unknown.png",
       "7호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846742232809574/unknown.png",
       "8호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846557180121158/8.png",
       "9호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846555741454416/9.png",
       "경의중앙선":"https://cdn.discordapp.com/attachments/995846401953103894/995846556035072120/2520997d8d784699.png",
       "경준선":"https://cdn.discordapp.com/attachments/995846401953103894/995846556257361962/3772d15b174ccb98.png",
       "공항철도":"https://cdn.discordapp.com/attachments/995846401953103894/995846556504821870/3d6d8d72012a38be.png",
       "분당선":"https://cdn.discordapp.com/attachments/995846401953103894/995846556739715172/5f0510ccc7917770.png",
       "신분당선":"https://cdn.discordapp.com/attachments/995846401953103894/995846556966199337/04f6a4fedff60b72.png",
       "우이신설선":"https://cdn.discordapp.com/attachments/995846401953103894/995846577119821824/827eabbd4c5d6605.png",
       "자기부상선":"https://cdn.discordapp.com/attachments/995846401953103894/995846577350512660/6ae5b62834f9bc80.png"
       }

response = requests.get(url)
result = json.loads(response.text)
for element in result["realtimeArrivalList"]:
        print(line[element["subwayId"]])
        print(element["trainLineNm"])
        if(element["btrainSttus"]!=None):
                print(element["btrainSttus"])
        if(int(element["barvlDt"])>=60):        
                print(math.trunc(int(element["barvlDt"])/60),"분",int(element["barvlDt"])%60,"초")
        else:
                print(element["barvlDt"]+"초")
        print(element["statnNm"])
        print(element["arvlMsg2"])
        print(element["arvlMsg3"])
        print(arrivalCode[element["arvlCd"]])
        print("-----------------")