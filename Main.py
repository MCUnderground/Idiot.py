import random
import discord


client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as ", client.user.name, ' ', client.user.id)


@client.event
async def on_message(message):
    if message.content.startswith("%MCWorld"):
           await client.send_message(message.author, "GO TO HELL")
    if message.content.startswith("%help"):
        await client.send_message(message.author, "PREFIX: %\nhelp - Help command\ntest - Dont do it\nroll - Test your luck on scale 1 to 100!\nsexy - Get scared, or get up ;)")
    if message.content.startswith("%test"):
        await client.send_message(message.channel, "HAIL HITLER")
    if message.content.startswith("%roll"):
        await  client.send_message(message.channel, random.randrange(0, 100))
    if message.content.startswith("%sexy"):
        sexy = [
            "images/img01.jpg","images/img02.jpg","images/img03.jpg","images/img04.jpg","images/img05.jpg"]
        await  client.send_file(message.channel, random.choice(sexy))


client.run('')
