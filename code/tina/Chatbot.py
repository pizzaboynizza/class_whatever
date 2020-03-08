import discord
from discord.ext import commands

#On_Ready is called when the client is done preapring data received from discord, Its when the bot login
@bot.eventasync def on_ready():
    print('logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def green(ctx):
    awaut ctx.send(":smiley: :wave: Hello, There!")


@bot.cmmands()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")