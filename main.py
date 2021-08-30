import discord
import os
import requests
import json
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import randfacts
import random
import pyjokes
from discord import ChannelType, Guild, Member, Message, Role, Status, utils, Embed
from add import token
from mongo import *



global annoy
annoy = True

client = discord.Client()

dood = ["what is a random fact about you?","what food do you like?","how was your day in school/office","how was your last vacation","have you completed your homework/office work?",
"what do you like to do most?","what was your latest dream?","what do you like doing?","what do you want to do?","who is your idol","who do you hate the most"]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    activity_string = '{} servers.'.format(len(client.guilds))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_string))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )



global meme
meme = 0



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    global award
    award = False

    global meme
    meme = meme + 1
    #print(meme)

    if message.content.startswith(">stop_a"):
        global annoy
        annoy = False
        await message.channel.send("STOPPED ANNOY!")

    if message.content.startswith(">start_a"):
        annoy = True
        await message.channel.send("STARTED ANNOY!")


    if annoy == True:
        if message.content.startswith('lol') or message.content.startswith('LMAO') or message.content.startswith('LOL') or message.content.startswith('Lmao') or message.content.startswith('Lol'):
            await message.channel.send(':rofl:')
        elif message.content.startswith('~grab'):
            await message.channel.send("MONEYYY $$$$$$$$$$$")
        elif message.content.startswith('bruh') or message.content.startswith("Bruh") or message.content.startswith("BRUH") or message.content.startswith(r"BR*H") or message.content.startswith(r"br*h"):
            await message.channel.send("yes, very bruh indeed")
        elif message.content.startswith('ihni'):
            await message.channel.send("get an idea, bro, or else youll end up like pranay")
        elif message.content.startswith(r"srsly") or message.content.startswith("srsly?") or message.content.startswith("srsly??"):
            await message.channel.send("oh no, *smriti vibes are back*")
        elif message.content.startswith("ikr") or message.content.startswith("IKR") or message.content.startswith("ifkr") or message.content.startswith("IFKR"):
            await message.channel.send("even ik!")
        elif message.content.startswith("bye") or message.content.startswith("bye") or message.content.startswith("ok bai"):
            await message.channel.send("dont leave :(")
        elif message.content.startswith("no u") or message.content.startswith("No u") or message.content.startswith("NO U"):
            await message.channel.send("no u")
        elif message.content.startswith("-_-"):
            await message.channel.send("`-__________________________-`")
        elif message.content.startswith('oof') or message.content.startswith("OOF"):
            await message.channel.send("OOF!")
        elif message.content.startswith("why") or  message.content.startswith("Why") or  message.content.startswith("WHY"):
            await message.channel.send("why not?")
        elif message.content.startswith("what is school?"):
            await message.channel.send("Its a modern version of a gulag with potrays a juxtaposition in children")
    else:
        pass

    if message.content.startswith(">help"):
        embed=discord.Embed(title="Hello!, I am nachos bot!", color=0x00ff00)
        embed.add_field(name=">inspire", value="to give you zenquotes", inline=True)
        embed.add_field(name=">fact", value="to tell you a fact", inline=True)
        embed.add_field(name=">ask", value="to ask you a question", inline=True)
        embed.add_field(name=">joke", value="for chuck norris jokes", inline=True)
        embed.add_field(name=">info", value="Information about you", inline=True)
        embed.add_field(name=">censor [word]",value="To censor words (ADMIN ONLY)", inline=True)
        embed.add_field(name=">delete [word]",value="To stop censoring a word (ADMIN ONLY)",inline=True)
        embed.add_field(name=">words",value="To see the words you cant use",inline=True)
        #embed.add_field(name=">list", value="to show you how much discord you use", inline=True)
        embed.add_field(name="To help us add more features,", value="join our discord: https://discord.gg/dPXXPdpYYZ")

        await message.channel.send(embed=embed)


    if message.content.startswith(">censor"):
        if message.author.guild_permissions.administrator == True:
            x = message.content
            insert(x[8:],message.author.guild.id,message.author.id)
            await message.channel.send("ADDED!")
        else:
            await message.channel.send("sorry, only admins can add words")
    elif message.content.startswith(">delete"):
        if message.author.guild_permissions.administrator == True:
            x = message.content
            delete_word(x[8:],message.author.guild.id)
            await message.channel.send("OK DONE")
        else:
            message.channel.send("sorry, only admins can delete words")



    if message.content.startswith(">words"):
        x = get_word(message.author.guild.id)
        await message.channel.send(str(x))

    if message.content.startswith(">joke"):
        My_joke = pyjokes.get_joke(language="en", category="all")
        await message.channel.send(My_joke)

    if message.content.startswith(">fact"):
        x = randfacts.get_fact()
        embed=discord.Embed(color=0x00ff00)
        embed.add_field(name="Did you know?",value=x,inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith('>inspire'):
        quote = get_quote()
        embed=discord.Embed(color=0x00ff00)
        embed.add_field(name="A quote",value=quote,inline=True)
        await message.channel.send(embed=embed)
        #await client.change_presence(activity=discord.Game(quote))


    if message.content.startswith(">list"):
        embed = discord.Embed(color=0x00ff00)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="THIS FEATURE HAS BEEN REMOVED", value="sed",inline=True)
        await message.channel.send(embed=embed)






    elif message.content.startswith(">save"):
        await message.channel.send("ok, saving......")
        cll()
        namebluh()
        for i in list:
            iiii(i)
        await message.channel.send("done!")

    if message.content.startswith(">info"):
        if message.author.bot == False:
            roles = [role for role in message.author.roles]
            mom = message.author.name + "#" + message.author.discriminator
            embed=discord.Embed(title="User Info", color=0x00ff00)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.add_field(name="Username", value=mom, inline=True)
            embed.add_field(name="User ID", value=message.author.id)
            embed.add_field(name="Nickname:", value=message.author.nick, inline=True)
            embed.add_field(name="Server", value=message.author.guild, inline=True)
            embed.add_field(name="Roles", value=f" ".join([role.mention for role in roles]), inline=True)
            #embed.add_field(name="Platform", value=f"{'Mobile' if message.author.is_on_mobile() else 'PC'}", inline=True)
            embed.add_field(name="Registered at:", value=message.author.created_at.strftime('%a, %#d %B %Y, %I:%M %p'), inline=True)
            embed.add_field(name="Joined this server on:", value=message.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"), inline=True)
            embed.add_field(name="Admin?", value=f"{message.author.guild_permissions.administrator}", inline=True)
            #embed.add_field(name="No. of Messages:", value=mes, inline=True)
            embed.set_footer(text=f"Requested by: {message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("BOTS ARE NOT INVITED!")

    z = message.content
    r = get_word(message.author.guild.id)
    for p in r:
        for j in z.split(' '):
            if p == j:
                await message.channel.send("YOU SAID A BAD WORD")
                await message.delete()



client.run(token)
