import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async  def on_ready():
    print("Loggend in bot", bot.user.name)
    print("Bot id ", bot.user.id)
    print("connection was succesful!")
    print("=" * 30)

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕")

bot.run("OTkwOTkxODg1MDcxOTc0NDcw.GF8N89.rr5gVjfQ4WX4rEa5o3zQZdBRkw7BhmZ8YvHISA")
