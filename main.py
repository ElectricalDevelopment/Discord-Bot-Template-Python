import discord
from discord.ext import commands

bot = commands.prefix(command_prefix='!', case_insensitive=True)

@bot.event
async def on_ready():
  print(f'{bot.user} is online and ready!')
  
@bot.command()
async def hello(ctx):
  await ctx.send('Hello human!')

bot.run('put your token here.')
