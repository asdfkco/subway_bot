import json
import discord
import requests
import math
import time
from discord.ext import commands
from datetime import datetime

now = datetime.now()

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
       "6호선":"https://cdn.discordapp.com/attachments/995846401953103894/995846556739715172/5f0510ccc7917770.png",
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
    
img_number = {"1호선":"https://cdn.discordapp.com/attachments/997167061908336820/997169555602415647/images-removebg-preview-removebg-preview-removebg-preview.png",
       "2호선":"https://cdn.discordapp.com/attachments/997167061908336820/997169514502434836/images__1_-removebg-preview.png",
       "3호선":"https://cdn.discordapp.com/attachments/997167061908336820/997169556244148264/-removebg-preview.png",
       "4호선":"https://cdn.discordapp.com/attachments/997167061908336820/997169514775060590/1_-removebg-preview.png",
       "5호선":"https://cdn.discordapp.com/attachments/997167061908336820/997169514036867142/2_-removebg-preview.png",
       "6호선":"https://cdn.discordapp.com/attachments/997167061908336820/997169513793589292/3_-removebg-preview.png",
       "7호선":"https://cdn.discordapp.com/attachments/997167061908336820/997169513499992165/4_-removebg-preview.png",
       "8호선":"https://cdn.discordapp.com/attachments/997167061908336820/997169555317194762/5_-removebg-preview.png",
       "9호선":"https://cdn.discordapp.com/attachments/997167061908336820/997169554654503043/images__2_-removebg-preview.png",
       "경의중앙선":"https://cdn.discordapp.com/attachments/997167061908336820/997169515039297617/8_preview_rev_1_1.png",
       "경춘선":"https://cdn.discordapp.com/attachments/997167061908336820/997169515303546960/10_-removebg-preview_preview_rev_1_1.png",
       "공항철도":"https://cdn.discordapp.com/attachments/997167061908336820/997169556768436254/9_-removebg-preview.png",
       "분당선":"https://cdn.discordapp.com/attachments/997167061908336820/997169514238185473/images__3_-removebg-preview.png",
       "신분당선":"https://cdn.discordapp.com/attachments/997167061908336820/997169555937968188/6_-removebg-preview.png",
       "우이신설선":"https://cdn.discordapp.com/attachments/997167061908336820/997169556499992596/11_-removebg-preview.png",
       "자기부상선":"https://cdn.discordapp.com/attachments/997167061908336820/997169556499992596/11_-removebg-preview.png"
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
        # with open ("./token/신정(은행정).json", "r",encoding="UTF-8") as f:
                # result = json.load(f)
        
        location = message.content.replace("!","").replace("역","")
        try:
                url = f"http://swopenAPI.seoul.go.kr/api/subway/{key}/json/realtimeStationArrival/1/6/{location}"
                print(location)
                response = requests.get(url)
                result = json.loads(response.text)
                print(url)

                global time_
                time_ = "_ _"
                num=1   
        # 마지막으로 겹치는건 2개로해보기
        # 4개만 제한둔다
                if(len(result["realtimeArrivalList"][1]["subwayList"])==1):
                        for element in result["realtimeArrivalList"]:
                                if(num==4):    
                                        break       
                                time.sleep(0.5)
                                # 2~9호선만 도착시간 뜸
                                if(int(element["barvlDt"])>=60):      
                                        if(int(element["barvlDt"])%60 == 0):
                                                time_ = str(math.trunc(int(element["barvlDt"])/60))+"분 "
                                        elif(int(element["barvlDt"])%60 != 0):
                                                time_ = str(math.trunc(int(element["barvlDt"])/60))+"분 "+str(int(element["barvlDt"])%60)+"초"
                                else:
                                        time_ = element["barvlDt"]+"초"
                                embed = discord.Embed(title=element["statnNm"], color=0xAAFFFF)
                                if(time_!="0초"):
                                        embed.add_field(name=element["trainLineNm"].replace(" - ","\n"), value="_ _", inline=False)
                                        embed.add_field(name="도착까지 남은시간 : "+time_, value="_ _", inline=False)
                                else:        
                                        embed.add_field(name=element["trainLineNm"].replace(" - ","\n"), value="_ _", inline=False)
                                        embed.add_field(name=element["arvlMsg2"], value="_ _", inline=False)
                                embed.add_field(name=element["arvlMsg2"], value="_ _", inline=False)
                                embed.add_field(name="종점역 - "+element["bstatnNm"], value=arrivalCode[element["arvlCd"]], inline=False)
                                if(element["btrainSttus"]!=None):
                                        embed.set_footer(text=element["btrainSttus"])
                                embed.set_thumbnail(url=img_number[line[element["subwayId"]]])
                                embed.set_image(url=img_train[line[element["subwayId"]]])
                                print(element["subwayId"])
                                await message.channel.send(embed=embed)   
                                num+=1
                
                        
                        
                else:
                        for element in result["realtimeArrivalList"]:
                                        time.sleep(0.5)
                                        # 2~9호선만 도착시간 뜸
                                        if(int(element["barvlDt"])>=60):      
                                                if(int(element["barvlDt"])%60 == 0):
                                                        time_ = str(math.trunc(int(element["barvlDt"])/60))+"분 "
                                                elif(int(element["barvlDt"])%60 != 0):
                                                        time_ = str(math.trunc(int(element["barvlDt"])/60))+"분 "+str(int(element["barvlDt"])%60)+"초"
                                        else:
                                                time_ = element["barvlDt"]+"초"
                                        embed = discord.Embed(title=element["statnNm"], color=0xAAFFFF)
                                        if(time_!="0초"):
                                                embed.add_field(name=element["trainLineNm"].replace(" - ","\n"), value="_ _", inline=False)
                                                embed.add_field(name="도착까지 남은시간 : "+time_, value="_ _", inline=False)
                                        else:        
                                                embed.add_field(name=element["trainLineNm"].replace(" - ","\n"), value="_ _", inline=False)
                                                embed.add_field(name=element["arvlMsg2"], value="_ _", inline=False)
                                        embed.add_field(name="종점역 - "+element["bstatnNm"], value=arrivalCode[element["arvlCd"]], inline=False)
                                        if(element["btrainSttus"]!=None):
                                                embed.set_footer(text=element["btrainSttus"])
                                        embed.set_thumbnail(url=img_number[line[element["subwayId"]]])
                                        embed.set_image(url=img_train[line[element["subwayId"]]])
                                        print(element["subwayId"])
                                        await message.channel.send(embed=embed)
                        
                                
        except KeyError as e:
                print(e)
                if(now.hour >= 0 and now.hour < 6):
                        await message.channel.send("막차가 끊겼거나 존재하지 않는 역입니다.")
                else:
                        await message.channel.send("존재하지 않는 역입니다.")
    



client.run(token["token"])



