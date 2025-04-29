import discord
from discord.ext import commands

# Set up bot command prefix and intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}.')

@bot.command()
async def hi(ctx):
    await ctx.send("Hi!")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')