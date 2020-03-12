


@client.event
async def on_message(message):
    if message.content == ".img": # Replace .img with whatever you want the command to be

        imgList = os.listdir("./All_Images") # Creates a list of filenames from your folder

        imgString = random.choice(imgList) # Selects a random element from the list

        path = "./All_Images/" + imgString # Creates a string for the path to the file

        await client.send_file(message.channel, path) # Sends the image in the channel the command was used


