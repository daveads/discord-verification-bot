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


    """
    # Testing
    channel = bot.get_channel(1054400575170678825)
    c = []
    async for m in channel.history(limit=100):
        for i in m.embeds:
            a = i.to_dict()
            c.append(a['footer']['text'])
    
    print(c)

    if '840152379122384896' in c:
        print("verification pending")

    """
    
async def main():
    await bot.start(os.getenv('token'))
    
    

asyncio.run(main())