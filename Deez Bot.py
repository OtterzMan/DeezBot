import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import click

client = Bot(description="Deez Nuts", command_prefix="N.", pm_help = False)

###cls event###
def cls():
    click.clear()
###############



@client.event
async def on_ready():
	print('Logged in Succsefully')
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')

'''@client.event
async def on_message(message):
    if message.content.includes ("dad"):
        await message.send("TOM HAS NO DAD, WHAT A FATHERLESS CHILD") <--- DIDN'T WORK '''

@client.command()
async def test(ctx):
	await ctx.send("icles")

botinvite = 'https://bit.ly/DeezNutzBot'

@client.command()
async def helper(ctx):
	await ctx.send("Alright i will help you")
	await ctx.send("""
彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡
------------------------
     DEEZ BOT 420
------------------------

Prefix = """ + client.command_prefix + """
Author = Øtterz#2001
Invite = """ + botinvite + """
彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡彡
""")

@client.command()
async def deezify(ctx, *, message):

	if message[-1] == "e":
		await ctx.send (message + "!! more like " + message + "eez NUTS")

	if message[-1] == "y":
		await ctx.send (message + "!! more like " + message + "eez NUTS")
	
	if message[-1] == "l":
		await ctx.send (message + "!! more like " + message + "yeez NUTS")

	if message[-1] == "a":
		await ctx.send (message + "!! more like " + message + "ma BALLS")


client.run('BOT TOKEN GOES HERE')
