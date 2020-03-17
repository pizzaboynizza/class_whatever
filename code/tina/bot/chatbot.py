import discord
from discord.ext import commands
import random
import requests
from discord.utils import get
import asyncio




#This set the precommand for the bot, This is how you call the bot to action
bot = commands.Bot(command_prefix='$')

#async and await are a event loop


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
    #Passes function contrl back to the event loop, its like return but it will send to the channel
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def keycat(ctx):
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


@bot.command(pass_context=True)
async def giverole(ctx,user: discord.Member, role:discord.Role):
    await user.add_roles(role)
    await ctx.send("Done")

#a syntax for storing and exchanging data
# I am sending a request to the website to request/get a random joke from the site and only return if status code == 200
@bot.command()
async def joke(ctx):
    chuckJoke = requests.get('http://api.icndb.com/jokes/random?')
    if chuckJoke.status_code == 200:
        chuckJoke = chuckJoke.json()['value']['joke']
        await ctx.send(chuckJoke)
        await ctx.send("Did you enjoy that joke? HAHAHAHA :rofl:")


#This website was giving me a list of link coming from json, so using the index [0] it will pull the first thing out of the list and posted it. 
@bot.command()
async def dog(ctx):
    dog = requests.get('https://dog.ceo/api/breeds/image/random/1')
    if dog.status_code == 200:
        cat = dog.json()['message'][0]
        await ctx.send(cat)
        await ctx.send("Did you enjoy that CAT? Meoww :cat:")
        await ctx.send("Lol Jk it's a dog..:dog:")


#JavaScript Object Notation
#This website give an API in a list of dic, you have to use [0] to pull it out of the list and then use the key in the dic to grab the url to post to the channel, whinch happen to be url
@bot.command()
async def cat(ctx):
    dog = requests.get('https://api.thecatapi.com/v1/images/search')
    if dog.status_code == 200:
        cat = dog.json()[0]['url']
        await ctx.send(cat)
        await ctx.send("Did you enjoy that CAT? Meoww :cat:")
        




@bot.command()
async def kick(ctx,member:discord.Member, *, reason='one'):
    await member.kick(reason=reason)


@bot.command()
async def ban(ctx,member:discord.Member, *, reason= 'None'):
    await member.ban(reason=reason)




bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Wow cat bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$keycat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    embed.add_field(name="$slap", value="Give someone a little touch", inline=False)
    embed.add_field(name="$word", value="Bot will copy what you say", inline=False)
    embed.add_field(name="$giverole rolename", value="bot will give you a role.", inline=False)
    embed.add_field(name="$joke", value="This bot tell the best Chuck Norris jokes", inline=False)
    embed.add_field(name="$dog", value="Best Dog picture ever", inline=False)
    embed.add_field(name="$cat", value="Best Cat picture ever", inline=False)
    
    

    await ctx.send(embed=embed)
#remove token before commiting
bot.run('token')