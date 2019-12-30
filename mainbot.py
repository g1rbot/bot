import discord 
import wikipedia
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.command()
async def wiki(ctx, *, words):
    await ctx.send(wikipedia.page(words).url)


@client.command()
async def hello(ctx):
    await ctx.send('UwU elllo')


@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@client.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: hehe, HI there :3!")

@client.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@client.command()
async def info(ctx):
    embed = discord.Embed(title="G1R", description="here to serve you master UwU.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name=".add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name=".multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name=".greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name=".cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name=".info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name=".help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)



@client.event 
async def on_ready():
    print("the bot is ready")
client.run("#TOKEN GOES HERE")




