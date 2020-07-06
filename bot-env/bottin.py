import discord
from discord.ext import commands
from discord.utils import get
import os
import youtube_dl
import maths
import private


client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    chGeneral = client.get_channel(85103220216561664)
    voice = await chGeneral.connect()
    print()
    print('Bot Ready')
    print()
    print(voice)
    print()
    print('Awaiting Commands')
    print()
    print('-----------------------------------------')


@client.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()


@client.command()
async def helpme(ctx, arg1):
    await ctx.send(f'What is {arg1}?')


@client.command()
async def ding(ctx):
    playsound(ctx, "./sounds/Ding.mp3", .5)


@client.command()
async def conspire(ctx):
    playsound(ctx, "./sounds/Conspiracy.mp3", .5)


@client.command()
async def shit(ctx):
    playsound(ctx, "./sounds/Shit.mp3", 1)


@client.command()
async def gotcha(ctx):
    playsound(ctx, "./sounds/Gotcha.mp3", .5)


@client.command()
async def dev(ctx):
    playsound(ctx, "./sounds/Dev.mp3", .7)


@client.command()
async def admit(ctx):
    playsound(ctx, "./sounds/Admit.mp3", .7)


@client.command()
async def daddy(ctx):
    playsound(ctx, "./sounds/Daddy.mp3", 1)


@client.command()
async def getout(ctx):
    playsound(ctx, "./sounds/GetOut.mp3", 1)


@client.command()
async def knock(ctx):
    playsound(ctx, "./sounds/Knock.mp3", 1)


def playsound(ctx, path, volume):
    mpExists = os.path.isfile(path)
    if mpExists:
        voice = get(client.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(path))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume


client.run(private.pToken)
