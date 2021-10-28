import discord
import pyfiglet
from discord.ext import commands as zeenode
import asyncio
import random


class mass(zeenode.Cog):
    def __init__(self, bot):
        self.bot = bot

    @zeenode.command()
    async def massreact(self, ctx, emote):
        await ctx.message.delete()
        messages = await ctx.message.channel.history(limit=20).flatten()
        for message in messages:
            await message.add_reaction(emote)

    @zeenode.command()
    async def spam(self, ctx, amount: int = None, delay: float = None, *, message: str = None):
        await ctx.message.delete()
        salt = random.choice(range(1, 10))
        extraSalt = random.choice(range(20, 30))
        superExtraSalt = random.choice(range(60, 120))
        EsuperExtraSalt = random.choice(range(120, 240))
        epic = random.choice(range(300, 500))
        list = [salt, extraSalt, superExtraSalt, EsuperExtraSalt, epic]
        print(list)
        choser = random.choice(range(1, 4))
        for each in range(0, amount):
            await ctx.send(f"{message}")
            await asyncio.sleep(delay)


def setup(bot):
    bot.add_cog(mass(bot))
