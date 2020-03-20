# bot.py
import os
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands

from itemSearch import item_scraping

#obtain the code for the bot authentication
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#the prefix to do a command is !
bot = commands.Bot(command_prefix='!')
print(f"DatBoi has connected")

#scraping the website below, and uses itemSearch.py for output info
@bot.command(name='ff', help=f"Finds item on https://ffxiv.gamerescape.com, has to have correct spelling")
async def itemsearch(ctx, *message):
	mess = await ctx.send("Currently loading information")
	output = ""
	for entry in message:
		output += f"{entry} "
	response = item_scraping(output)
	await mess.edit(content = response)

#posts the oceanfishing image
@bot.command(name='of')
async def oceanfishing(ctx):
	with open('oceanfishing.png', 'rb') as fp:
		await ctx.send(file=discord.File(fp, 'oceanfishing.png'))

#dices 
failMessage = "You rolled a 1 loser"
@bot.command(name='d6')
async def d6(ctx):
	num = str(random.choice(range(1,6)))
	output = f"You rolled a {num}"
	if '1' in num:
		output = failMessage
	await ctx.send(output)

@bot.command(name='d20')
async def d6(ctx):
	num = str(random.choice(range(1,20)))
	output = f"You rolled a {num}"
	if '1' in num:
		output = failMessage
	await ctx.send(output)

@bot.command(name='d100')
async def d6(ctx):
	num = str(random.choice(range(1,100)))
	output = f"You rolled a {num}"
	if '1' in num:
		output = failMessage
	await ctx.send(output)

#makes the bot quit
@bot.command(name='quit')
async def quitCommand(ctx):
	await bot.logout()

#Outputs the following when a command is not found
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CommandNotFound):
		await ctx.send('Command not found')

bot.run(token)
