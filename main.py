import json
import discord
import requests
import math
import time
from discord.ext import commands

with open ("./token/token.json", "r") as f:
    token = json.load(f)
    
key = token["key"]

global line,arrivalCode,img

line = {"1001":"1호선","1002":"2호선","1003":"3호선","1004":"4호선","1005":"5호선","1006":"6호선","1007":"7호선","1008":"8호선","1009":"9호선","1075":"분당선","1077":"신분당선","1091":"자기부상선"
        ,"1092":"우이신설선","1063":"경의중앙선","1065":"공항철도","1067":"경춘선"}      

arrivalCode = {"0":"진입", "1":"도착", "2":"출발", "3":"전역출발", "4":"전역진입", "5":"전역도착", "99":"운행중"}

img_train = {"1호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846742421541077/unknown.png",
       "2호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846742652231790/unknown.png",
       "3호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846742832590999/unknown.png",
       "4호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846743071657984/unknown.png",
       "5호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846743264600114/unknown.png",
       "6호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846743457546280/unknown.png",
       "7호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846742232809574/unknown.png",
       "8호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846557180121158/8.png",
       "9호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846555741454416/9.png",
       "경의중앙선":"https://cdn.discordapp.com/attachments/995846401953103894/995846556035072120/2520997d8d784699.png",
       "경춘선":"https://cdn.discordapp.com/attachments/995846401953103894/995846556257361962/3772d15b174ccb98.png",
       "공항철도":"https://cdn.discordapp.com/attachments/995846401953103894/995846556504821870/3d6d8d72012a38be.png",
       "분당선":"https://cdn.discordapp.com/attachments/995846401953103894/995846556739715172/5f0510ccc7917770.png",
       "신분당선":"https://cdn.discordapp.com/attachments/995846401953103894/995846556966199337/04f6a4fedff60b72.png",
       "우이신설선":"https://cdn.discordapp.com/attachments/995846401953103894/995846577119821824/827eabbd4c5d6605.png",
       "자기부상선":"https://cdn.discordapp.com/attachments/995846401953103894/995846577350512660/6ae5b62834f9bc80.png"
       }
    
img_number = {"1호선":"https://cdn.discordapp.com/attachments/995846401953103894/996255926988316692/images.png",
       "2호선":"https://cdn.discordapp.com/attachments/995846401953103894/996255927781040201/images_1.png",
       "3호선":"https://cdn.discordapp.com/attachments/995846401953103894/996255895182909440/1a9a0538bae6e7a8.png",
       "4호선":"https://cdn.discordapp.com/attachments/995846401953103894/996255927273541734/1.png",
       "5호선":"https://cdn.discordapp.com/attachments/995846401953103894/996255927583912018/2.png",
       "6호선":"https://cdn.discordapp.com/attachments/995846401953103894/996255893488402452/3.png",
       "7호선":"https://cdn.discordapp.com/attachments/995846401953103894/996255893689733220/4.png",
       "8호선":"https://cdn.discordapp.com/attachments/995846401953103894/996255893899452466/5.png",
       "9호선":"https://cdn.discordapp.com/attachments/995846401953103894/996255927994962001/images_2.png",
       "경의중앙선":"https://cdn.discordapp.com/attachments/995846401953103894/996255894427934820/8.png",
       "경춘선":"https://cdn.discordapp.com/attachments/995846401953103894/996255894918664212/10.png",
       "공항철도":"https://cdn.discordapp.com/attachments/995846401953103894/996255894641836082/9.png",
       "분당선":"https://cdn.discordapp.com/attachments/995846401953103894/996255928183689306/images_3.png",
       "신분당선":"https://cdn.discordapp.com/attachments/995846401953103894/996255894079815720/6.png",
       "우이신설선":"https://cdn.discordapp.com/attachments/995846401953103894/996255894255972372/7.pngㅇㅁㅁㅋㅋㅋㅋㅋㅋㅋㅁㅁㅁㅁㅁㅋ",
       "자기부상선":"https://cdn.discordapp.com/attachments/995846401953103894/996268721574260836/11.png"
       }    
    
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Loggend in Bot: ', client.user.name)
    print('Bot id: ', client.user.id)
    print('connection was succesful!')
    print('=' * 30)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!"):
        location = message.content.replace("!","")
        url = f"http://swopenAPI.seoul.go.kr/api/subway/{key}/json/realtimeStationArrival/1/6/{location}"
        print(location)
        response = requests.get(url)
        result = json.loads(response.text)
        print(url)
        
        
        
        ### 그 뭐냐 머시기 0초는 안뜨게 하기
        global time_
        time_ = "_ _"
        for element in result["realtimeArrivalList"]:
                time.sleep(1)
                # 2~9호선만 도착시간 뜸
                if(int(element["barvlDt"])>=60):        
                        time_ = str(math.trunc(int(element["barvlDt"])/60))+"분"+str(int(element["barvlDt"])%60)+"초"
                else:
                        time_ = element["barvlDt"]+"초"
                embed = discord.Embed(title=element["statnNm"], color=0xAAFFFF)
                if(time_!="0초"):
                        embed.add_field(name=element["trainLineNm"], value=time_, inline=False)
                else:        
                        embed.add_field(name=element["trainLineNm"], value="_ _", inline=False)
                embed.add_field(name=element["arvlMsg2"], value="_ _", inline=False)
                embed.add_field(name=element["bstatnNm"], value=arrivalCode[element["arvlCd"]], inline=False)
                if(element["btrainSttus"]!=None):
                        embed.set_footer(text=element["btrainSttus"])
                embed.set_thumbnail(url=img_number[line[element["subwayId"]]])
                embed.set_image(url=img_train[line[element["subwayId"]]])
                print(element["subwayId"])
                await message.channel.send(embed=embed)
        
                
    



client.run(token["token"])



