import discord
from discord.ext import commands
import random
import requests


bot = commands.Bot(command_prefix='$')

@bot.event
# this is logged in the bot with commandline. 
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
#def a bot command say hey, take a(user input) and b(user input) and add them togeather. 
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat1(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

#ARG will pass whatever the user word is and the bot will report it, To copy more then one word, You must use "around" the word, Add the * star in to the () allow many argument to be passed in.
@bot.command()
async def word(ctx,*,arg):
    await ctx.send(arg)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Amazing bot", description="He's a work in progress, Soon will bring you all the cat facts.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Soda:D", value="Soda#0546")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discord.gg/XdDjFCx")

    await ctx.send(embed=embed)


# using bot command and picking a user from the discord self who enter a string of words after will output 'user' just got slapped for blah
@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')


@bot.command()
async def cat(ctx):
        cat = getCat()
    await ctx.send(cat)
    


bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Wow cat bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    embed.add_field(name="$slap", value="Give someone a little touch", inline=False)
    embed.add_field(name="$word", value="Bot will copy what you say", inline=False)

    await ctx.send(embed=embed)
#remove token before commiting
bot.run('')