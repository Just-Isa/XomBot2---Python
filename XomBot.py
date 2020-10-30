import discord

import random

from discord import File


class MyClient(discord.Client):

    # Einloggen Methode
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep bop.")

    # Wenn Nachricht gepostet wird
    async def on_message(self, message):

        if message.author == client.user:
            return

        elif message.content.startswith("~cock"):
            cockSize = random.randint(0, 8)
            if (cockSize > 5 and cockSize < 8):
                await message.channel.send("Your cock is a MASSIVE " + str(cockSize) + " inches...")
            elif (cockSize < 5):
                await message.channel.send("Your cock is a MASSIVE " + str(
                    cockSize) + " inches... well maybe not MASSIVE but hey, thats average right?")
            else:
                await message.channel.send("Your cock is a MASSIVE " + str(cockSize) + " inches... GodDAMN")

        elif message.content.startswith("~flip"):
            flip = random.randint(0, 8)
            if(flip == 0):
                await message.channel.send("heads")
            else:
                await message.channel.send("tails")

        else:
            if "xom" in str(message.content).lower():
                await message.add_reaction("xom:768629261052411904")

            elif "tekken" in str(message.content).lower():
                await message.add_reaction("kms2:709460300096602112")

            elif "good bot" in str(message.content).lower() or "nice bot" in str(message.content).lower():
                await message.author.send("Thanks bud 👌🏻😂🔥")

            elif "berdux" in str(message.content).lower():
                await message.add_reaction("Xomdux:741251152120643599")

            elif "masku" in str(message.content).lower():
                await message.add_reaction("🇲")
                await message.add_reaction("🇦")
                await message.add_reaction("🇸")
                await message.add_reaction("🇰")
                await message.add_reaction("🇺")

            elif ":((" in str(message.content):
                await message.channel.send("https://i.pinimg.com/originals/e3/82/01/e38201822636168d1afcf07de2bed01f.png")

            elif "oof" in str(message.content):
                await message.channel.send(file=File("oof.mp3"))

    async def on_message_delete(self, message):
        print("Deleted Message: " + message.content + " , Deleted by: " + str(message.author) + " , in the " + str(message.channel) + " channel")

client = MyClient()
client.run("NzY4NTUyMTgyMzIwMjAxNzI5.X5CH_w.i1TGAqAc0SQeV-JsCa2Fvh0jsBA")
