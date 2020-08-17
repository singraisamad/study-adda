import discord
import os
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = "$")
client.remove_command('help') # removing default help command to add custom one

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.event
async def on_member_join(member):
    newbiesRole = discord.utils.get(member.guild.roles, name="newbies")
    servantsRole = discord.utils.get(member.guild.roles, name="servants")

    if member.bot:
        await member.add_roles(servantsRole)
    else:
        await member.add_roles(newbiesRole)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I don't have that command!")
    else:
        herupaErrorLogChannel = client.get_channel(694819625501720606)
        await herupaErrorLogChannel.send(f"{error}")

for filename in os.listdir('.\\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

def read_TOKEN():
    with open("TOKEN.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()
TOKEN = read_TOKEN()
    
client = discord.Client()
client.run(TOKEN)
