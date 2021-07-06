import discord
import os
from discord.ext import commands
# Also needs PyNaCl to be installed

# Just replit token. not important
token = os.environ['Tok']
# Bot command prefix
client = commands.Bot(command_prefix="!")
# Confirmation bot is ready
@client.event
async def on_ready():
  print('{0} is in bois!'.format(client.user))

# Connect to current voice channel
@client.command()
async def cum(message):
  vc = message.author.voice.channel
  await vc.connect()
# Connect to specific voice channel
@client.command(pass_context=True)
async def go(ctx, channel: discord.VoiceChannel):
  if ctx.voice_client is not None:
    return await ctx.voice_client.move_to(channel)
  await channel.connect()
# Messages a list of commands in text channel
@client.command()
async def sex(message):
  await message.channel.send('!cum, !go, !bye !kutta, !bloody, !suck')
# Messages an image in text channel
@client.command()
async def suck(message):
  await message.channel.send(file = discord.File('./Audio/succ.jpg'))
# Plays audio in connected voice channel
@client.command(pass_context=True)
async def kutta(ctx):
  server = ctx.message.guild.voice_client
  await server.play((discord.FFmpegPCMAudio('./Audio/kutta.mp3')))
# Plays audio in connected voice channel
@client.command(pass_context=True)
async def bloody(ctx):
  server = ctx.message.guild.voice_client
  await server.play((discord.FFmpegPCMAudio('./Audio/bloody.mp3')))
# Disconnects from voice channel
@client.command(pass_context=True)
async def bye(ctx):
  server = ctx.message.guild.voice_client
  await server.disconnect()

client.run(token)