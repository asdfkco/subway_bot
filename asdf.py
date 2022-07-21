
# import discord
# import json
# from discord.ext import commands


# with open ("./token/token.json", "r") as f:
#     token = json.load(f)
    
    
#     client = commands.Bot(command_prefix='!')

# @client.event
# async def on_ready():
#     print('Loggend in Bot: ', client.user.name)
#     print('Bot id: ', client.user.id)
#     print('connection was succesful!')
#     print('=' * 30)
    
    
    
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     # elif message.content.startswith("."):
#         # await message.channel.send(message.content)
#     elif message.author.id == 524523017620160523:
#         await message.channel.send(message.content)
        
        
    
    
# client.run(token["token"])

from flask import Flask, jsonify, request
import sys
import requests
import json
import math

application = Flask(__name__)

with open("./token/token.json", "r") as f:
    token = json.load(f)

key = token["key"]
location = ""
url = f"http://swopenAPI.seoul.go.kr/api/subway/{key}/json/realtimeStationArrival/0/8/{location}"

line = {"1001": "1호선", "1002": "2호선", "1003": "3호선", "1004": "4호선", "1005": "5호선", "1006": "6호선", "1007": "7호선",
        "1008": "8호선", "1009": "9호선", "1075": "분당선", "1077": "신분당선", "1091": "자기부상선"
    , "1092": "우이신설선", "1163": "경의중앙선", "1165": "공항철도", "1167": "경춘선"}

arrivalCode = {"0": "진입", "1": "도착", "2": "출발", "3": "전역출발", "4": "전역진입", "5": "전역도착", "99": "운행중"}


@application.route("/")
def hello():
    return "Hello goorm!"


@application.route('/message', methods=['POST'])
def Message():
    content = request.json['content']

    if (content != u""):
        location = content.replace("역", "")
        if (location == "효창공원"):
            location = "효창공원앞"
        elif (location == "천호"):
            location = "천호(풍납토선)"
        elif (location == "신정"):
            location = "신정(은행정)"
        elif (location == "이수"):
            location = "총신대입구(이수)"
        elif (location == "총신대입구"):
            location = "총신대입구(이수)"
        elif (location == ""):
            dataSend = {
                "message": {
                    "text": "역이름을 입력해주세요."
                }
            }
            return
        response = requests.get(url)
        result = json.loads(response.text)

        for element in result["realtimeStationArrival"]:
            if (element["btrainSttus"] != None):
                btrain = element["btrainSttus"]
            if (int(element["barvlDt"]) >= 60):
                time = math.trunc(int(element["barvlDt"]) / 60), "분", int(element["barvlDt"]) % 60, "초"
            else:
                time = element["barvlDt"] + "초"
            dataSend = {
                "message": {
                    "text": line[element["subwayId"]],
                    "text": element["trainLineNm"],
                    "text": btrain,
                    "text": time,
                    "text": element["statnNm"],
                    "text": element["arvlMsg2"],
                    "text": element["arvlMsg3"]
                }
            }
    return jsonify(dataSend)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
>>>>>>> 1a8b8d0946846b101e6a2e6f66c0a6f59ceacdc0
