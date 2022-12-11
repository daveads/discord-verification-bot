import asyncio
from discord.ext import commands
import discord
import os

from dotenv import load_dotenv
from src.core.startverify  import StartVerify
from src.core.bot   import VerificationBot
from src.core.config_parser import BotConfigs

load_dotenv()
bot = VerificationBot()
bot_configs = BotConfigs()

@bot.command()
@commands.is_owner()
async def prepare(ctx: commands.Context):
    await ctx.message.channel.purge(limit=5)
    await ctx.send(file=discord.File(bot_configs.verfi_image()), view=StartVerify(bot))


face = ['😉', '😗', '😱' , '😛', '😜', ]
hand = ['🖐️', '✋', '👌', '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👍', '👎']

@bot.command()
@commands.is_owner()
async def emoji(ctx: commands.Context):

    import random 
    emoji = f"{random.choice(face)} {random.choice(hand)}"
    
    await ctx.send(f"{emoji}")


async def main():
    await bot.start(os.getenv('token'))
    
    

asyncio.run(main())