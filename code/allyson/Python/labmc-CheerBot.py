## Discord App Idea ##

import discord
import secrets
import random

TOKEN = secrets.DToken  # Remember to get a Token

# This is an Asyncronous thing, meaning it does not work in a straight turn order....  like how a character with higher Speed or w/e in an RPG can more 2 or more times in a turn.  SERIOUSLY!!  WHY CAN THEY CAST ULTIMA 3x in a TURN!  WHYYYYYYYYYYYYYY!!!!!?!?!?!!?!?

teacher_role = None
classmate_role = None
default_role = None
this_server = None
list_of_newbies = []

client = discord.Client()  # Heh... Discord\


@client.event
async def on_ready():
    global teacher_role, classmate_role, default_role, this_server
    print("Logged on as", client.user)
    print(f"This bot is a member of these guilds {client.guilds}")
    for server in client.guilds:
        if server.name == "A Place For Fishy Chaos":
            this_server = server
    roles = this_server.roles
    for role in roles:
        if role.name == "Teacher":
            teacher_role = role
        elif role.name == "Classmate":
            classmate_role = role
    default_role = this_server.default_role


@client.event
async def on_member_join(user):
    global list_of_newbies
    list_of_newbies.append(user.id)
    await user.send("Welcome to the the Fishbowl!\nIdentify yourself (by name).")


@client.event
async def on_message(message):  # No talking to yourself
    if message.author == client.user:
        return
    if message.content == "!ping":
        await message.channel.send("pong")
    elif message.content == "!8ball":
        await message.channel.send(eight())
    elif message.content.lower() == "!hi":
        await message.channel.send(greet(message.author.name))
    elif message.content.lower() == "!cat":
        await message.channel.send(cat())
    elif message.content.lower() == "!code":
        await message.channel.send(code())
    elif message.content.lower() == "!assist":
        await message.channel.send(assist())
    elif "shit" in message.content.lower():
        await message.delete()
        await message.author.send("╰(⇀︿⇀)つ-]═─── \n En Garde Your Tongue!")
    elif message.content.lower() == "!rps":
        await rps(message)
    elif message.content.lower() == "!purge" and message.author.name == "Micro Fish":
        # Lets me (because I own this bot!)clean up the chat
        async for msg in message.channel.history(limit=20):
            await msg.delete()
    elif (
        message.content.lower() in ["!rock", "!paper", "!scissors"]
        and str(message.channel.type) == "private"
    ):
        await pwnd(message)
    elif (
        message.content.lower() in ["merritt", "austen", "sheri"]
        and str(message.channel.type) == "private"
        and (
            message.author not in teacher_role.members
            and message.author not in classmate_role.members
        )
    ):
        await moves_like_jagger(message)
    elif message.content.startswith("!"):
        await message.channel.send(catchall())


async def moves_like_jagger(message):
    member_object = this_server.get_member(message.author.id)
    await member_object.add_roles(teacher_role)
    await message.author.send("Welcome!")


def greet(D):  # OH HAI MARK!
    g = [
        "O HAI!",
        f"Oh Hi {D}!",
        ":smiley: :wave: Hello, there!",
        "Sup?",
        f"Velcome to my lair{D}",
        "https://media.giphy.com/media/cQ75oh2k0p5rSpur1L/giphy.gif",
        "Hello!",
        "Greetings",
        "Welcome",
        "Hi!",
    ]
    return random.choice(g)


def eight():  # Don't you want to know?
    x = [
        "As I see it, yes",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don’t count on it",
        "It is certain",
        "It is decidedly so",
        "Most likely",
        "My reply is no",
        "My sources say no",
        "Outlook good",
        "Outlook not so good",
        "Reply hazy try again",
        "Signs point to yes",
        "Very doubtful",
        "Without a doubt",
        "Yes",
        "Yes, definitely",
        "You may rely on it",
        "Don't swipe right",
        "Why ask me?",
        "Consult a psychiatrist... Please",
        "Out To Lunch",
        "*Sings* Money makes the world go round, and Bio-Terrorism is real bad!",
    ]

    return random.choice(x)


def cat():  # CATS!
    c = [
        "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
        "https://media.giphy.com/media/WXB88TeARFVvi/giphy.gif",
        "https://media.giphy.com/media/rwCX06Y5XpbLG/giphy.gif",
        "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif",
        "https://media.giphy.com/media/JRE3AvLsSRXg360F6l/giphy.gif",
        "https://media.giphy.com/media/p4xp4BjHIdane/giphy.gif",
        "https://media.giphy.com/media/33OrjzUFwkwEg/giphy.gif",
        "https://media.giphy.com/media/ND6xkVPaj8tHO/giphy.gif",
        "https://media.giphy.com/media/PqdfIrXEza6fC/giphy.gif",
        "https://media.giphy.com/media/wUgWRubJHS7Ac/giphy.gif",
        "https://media.giphy.com/media/EWKJvpuRlBocM/giphy.gif",
        "https://media.giphy.com/media/13HBDT4QSTpveU/giphy.gif",
        "https://media.giphy.com/media/LHZyixOnHwDDy/giphy.gif",
        "https://media.giphy.com/media/RsXdnbJ1tnjVK/giphy.gif",
        "https://media.giphy.com/media/3QC7uohUGL5mM/giphy.gif",
        "https://media.giphy.com/media/qoxM1gi6i0V9e/giphy.gif",
        "https://media.giphy.com/media/fQD5Y6bAT30lbQaPmE/giphy.gif",
        "https://media.giphy.com/media/3oEduQAsYcJKQH2XsI/giphy.gif",
        "https://media.giphy.com/media/XNdoIMwndQfqE/giphy.gif",
        "https://media.giphy.com/media/Z1kpfgtHmpWHS/giphy.gif",
        "https://media.giphy.com/media/6bAZXey5wNzBC/giphy.gif",
        "https://media.giphy.com/media/WPWrU2AeK3aV2/giphy.gif",
        "https://media.giphy.com/media/11AezGDEabmJBm/giphy.gif",
        "https://media.giphy.com/media/uZxa6mNaSihVu/giphy.gif",
        "https://media.giphy.com/media/6jwXl9wTwkS0E/giphy.gif",
        "https://media.giphy.com/media/MSSE2Irr1QaNG/giphy.gif",
        "https://media.giphy.com/media/13tks6KkV5Crzq/giphy.gif",
        "https://media.giphy.com/media/bfcGcG0ceYZva/giphy.gif",
        "https://media.giphy.com/media/p8oLmaysCjhVC/giphy.gif",
        "https://tenor.com/view/pusheen-me-idid-cookies-cookie-jar-gif-16547792",
    ]
    return random.choice(c)


def code():  # Coding stuff
    coco = [
        "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
        "https://media.giphy.com/media/xT1XGzXhVgWRLN1Cco/giphy.gif",
        "https://www.codewars.com",
        "https://www.freecodecamp.org",
        "https://www.theodinproject.com",
        "https://davidwalsh.name",
        "https://pdxcodeguild.com",
        "https://hackpledge.org",
        "https://dash.generalassemb.ly",
        "https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/tree/master/",
        "https://www.cs.hmc.edu/twiki/bin/view/CSforAll/",
        "https://medium.com/learning-journalism-tech/five-mini-programming-projects-for-the-python-beginner-21492f6ce0f3#.6pbjj4wur",
    ]
    return random.choice(coco)


# def rude():  # For censorship
#     resp = [
#         "https://media.giphy.com/media/iezZGa02IdjPqKQiKl/giphy.gif",
#         "https://media.giphy.com/media/7TrubccIZcImc/giphy.gif",
#         "https://media.giphy.com/media/V1ipAyt2Ovuqk/giphy.gif",
#     ]


def catchall():  # Whatever I haven't added
    fail = [
        "https://media.giphy.com/media/8r3oJi1omVvry/giphy.gif",
    ]
    return fail


def assist():  # help menu
    return """
HELP MENU
(ノಠ益ಠ)ノ彡┻━┻
!cat = Cat Gifs
!8ball = Magic-8Ball
!code = Coding Suprise
!rps = Rock Paper Scissors
!stuff = not yet implimented
"""


async def cen(message):

    new_message = str(message.content).replace("shit", "||shit||")
    await message.edit(content=new_message)


#     return


async def rps(message):
    await message.author.send(
        "Let's Play Rock + Paper + Scissors! \n Choose:  '!rock' '!paper' '!scissors' "
    )


async def pwnd(message):
    G = ["!rock", "!paper", "!scissors"]
    CheerBot = random.choice(G)
    d_message = message.content.lower()
    if d_message == CheerBot:
        await message.author.send("TIE!")
    elif d_message == "!rock" and CheerBot == "!scissors":
        await message.author.send("You win! Rock smashes Scissors!")
    elif d_message == "!scissors" and CheerBot == "!paper":
        await message.author.send("You Win! Scissors cut Paper (Like a beech)")
    elif d_message == "!paper" and CheerBot == "!rock":
        await message.author.send(
            "Okay, I admit it, you are better than I, but I have a secret\nI am not left handed."
        )
    elif d_message == "!rock" and CheerBot == "!paper":
        await message.author.send("CheerBot wins! CheeerBot best Bot!")
    elif d_message == "!scissors" and CheerBot == "!rock":
        await message.author.send("CheerBot wins! Scissors gets smashed yo!")
    elif d_message == "!paper" and CheerBot == "!scissors":
        await message.author.send("CheerBot wins! Paper-Cut!")
    return


client.run(TOKEN)
