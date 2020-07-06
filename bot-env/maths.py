import discord
from discord.ext import commands


client = commands.Bot(command_prefix="!maths")


@client.command()
async def add(ctx, arg1, arg2):
    equals = float(arg1) + float(arg2)
    await ctx.send(f'{arg1} + {arg2} = {equals}')
