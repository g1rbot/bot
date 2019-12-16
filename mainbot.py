import discord 
import wikipedia
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.command()
async def wiki(ctx, *, words):
    await ctx.send(wikipedia.page(words).url)


@client.event 
async def on_ready():
    print("the bot is ready")
client.run("")


