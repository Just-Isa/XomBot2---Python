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
            if(flip <= 4):
                await message.channel.send("heads")
            else:
                await message.channel.send("tails")

        elif message.content.startswith("~XomCry"):
            responses = [
                "You weren't ever perfect.\n You just had this self -\n That couldn't be plucked from a jar on the shelf.\n I can't even say just for sure what it was -\n Just something.\n Just something.\n Just something, because -\n You weren't ever perfect.\n You just had this style -\n Of making me laugh at your dumb little smile.\n I can't even say what it happened to be -\n Just something.\n Just something.\n Just something, you see -\n You weren't ever perfect.\n You just had this way -\n Of making me feel like it might be okay.\n I can't even say why I'm making this call.\n I miss you.\n I miss you.\n I miss you.\n \n That's all",
                "https://www.youtube.com/watch?v=ErmZRsCIUsE",
                "https://www.youtube.com/watch?v=Pt21dU5Pu8g",
                "https://www.youtube.com/watch?v=igVLTttJDnk",
                "https://www.youtube.com/watch?v=hYAQtEs2Img"
            ]
            await message.channel.send(random.choice(responses))

        elif message.content.startswith("~8Xom"):
            responses = [
                'Probably man idk',
                'If MoonMan blesses it',
                'Murray says just block it, aka. No.',
                'Donut says youre a retard',
                'Actually, yeah. Sure. I think so,',
                'I think that its possible, but im just a racist bot, so yknow...',
                'Femnomenal says no.',
                'Sometimes its okay to not ask questions you fucking idiot',
                'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAshutthefuckupAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                'It depends, ask my dad',
                'https://media.discordapp.net/attachments/797474866378440704/819865255889993738/unknown.png',
                'Sure.',
                'Yeah.',
                'Nah.',
                'I dont think so, maybe in the next life though.'
            ]
            await message.channel.send(random.choice(responses))

        else:
            if "tekken" in str(message.content).lower():
                await message.add_reaction("kms2:709460300096602112")

            elif "good bot" in str(message.content).lower() or "nice bot" in str(message.content).lower():
                await message.author.send("Thanks bud 👌🏻😂🔥")

            elif "masku" in str(message.content).lower():
                await message.add_reaction("🇲")
                await message.add_reaction("🇦")
                await message.add_reaction("🇸")
                await message.add_reaction("🇰")
                await message.add_reaction("🇺")

            elif ":((" in str(message.content):
                await message.channel.send("https://i.pinimg.com/originals/e3/82/01/e38201822636168d1afcf07de2bed01f.png")

            elif "~XomHelp" in str(message.content):
                await message.channel.send("Ill dm you my commands you bitch")
                await message.author.send("```md\n\n# You have these options:\n\n ~XomCry --> (WIP) \n\n ~8Xom --> Like an 8ball just with ME :D \n\n ~flip --> like a coinflip \n\n ~cock--> To measure your penis size (WIP), \n\n And there is some commands that are just for specific servers. So good luck finding those out lmao.\n\n # If you think you have some cool ideas mr isa up :) \n```")

            elif "xom" in str(message.content).lower():
                await message.add_reaction("xom:768629261052411904")
                
    async def on_message_delete(self, message):
        text_file = open("Deleted Messages.txt", "w")
        n = text_file.write("Deleted Message: " + message.content + " , Deleted by: " + str(message.author) + " , in the " + str(message.channel) + " channel")
        print("Deleted Message: " + message.content + " , Deleted by: " + str(message.author) + " , in the " + str(message.channel) + " channel")
        text_file.close()

client = MyClient()
client.run("NzY4NTUyMTgyMzIwMjAxNzI5.X5CH_w.jmHaLkxISX7rdHuCPXndZZEThlU")
