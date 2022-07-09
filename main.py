import discord,asyncio,json
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


with open("./token/token.json") as file:
    bot = json.load(file)
    token = bot["token"]

bot.run(token)
