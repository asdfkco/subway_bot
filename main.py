import discord
import asyncio
import numpy as np

from discord.ext import commands
client = commands.Bot(command_prefix='/')

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
    elif message.content.startswith('찬옥이'):
        await message.channel.send('응디 찰싹')

    if message.content.startswith("6호선"):
        embed = discord.Embed(title="6호선", description="6호선 시간표", color=0xAAFFFF)
        embed.add_field(name="응암순환행", value="2분후 도착 예정", inline=True)
        embed.add_field(name="응암순환행", value="5분후 도착 예정", inline=True)
        embed.add_field(name="응암순환행", value="8분후 도착 예정", inline=True)
        embed.add_field(name="봉화산행", value="1분후 도착 예정", inline=True)
        embed.add_field(name="봉화산행", value="4분후 도착 예정", inline=True)
        embed.add_field(name="봉화산행", value="8분후 도착 예정", inline=True)
        embed.set_footer(text="하단 설명")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/995846401953103894/995846743457546280/unknown.png")
        await message.channel.send(embed=embed)
        





# @client.command(name='주사위')
# async def roll(ctx, number):
#     await ctx.send('주사위 숫자 1에서 {}'.format(number))
#
#     result_number = np.random.randint(1, int(number)+1)
#     await ctx.send('결과 = {}'.format(result_number))
#
# @roll.error
# async def roll_error(ctx, error):
#     await ctx.send('아이 시팔 야이년아 제대로써 숫자')




client.run('OTk0NzU0MTcwNzU2Mjc2MzI1.GEmzLk.huDxJjv2VCBGnYn9yOP_VtgWRm_18gzQozAO7k')