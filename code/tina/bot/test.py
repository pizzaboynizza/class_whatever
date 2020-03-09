# class Slapper(commands.Converter):
#     async def convert(self, ctx,argument):
#         to_slap = random.choice(ctx.guild.members)
#         return (f'{3} slapped {1} because *{2}*',(ctx, to_slap, argument))

# @bot.command()
# async def slap1(ctx, * , reason:Slapper()):
#     await ctx.send(reason)


@client.event
async def on_message(message):
    if message.content == ".img": # Replace .img with whatever you want the command to be

        imgList = os.listdir("./All_Images") # Creates a list of filenames from your folder

        imgString = random.choice(imgList) # Selects a random element from the list

        path = "./All_Images/" + imgString # Creates a string for the path to the file

        await client.send_file(message.channel, path) # Sends the image in the channel the command was used


