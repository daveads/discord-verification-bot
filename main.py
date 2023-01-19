import asyncio
from discord.ext import commands
import discord
import os

from dotenv import load_dotenv
from src.core.startverify  import StartVerify
from src.core.bot   import VerificationBot
from src.core.config_parser import BotConfigs


from src.model import verfdb
# intializing database
verfdb.main()

load_dotenv()
bot = VerificationBot()
bot_configs = BotConfigs()


async def load():
    for f in os.listdir("cogs"):
        if f.endswith(".py"):
            await bot.load_extension(f'cogs.{f[:-3]}')



@bot.command()
@commands.is_owner()
async def prepv(ctx: commands.Context):
    await ctx.message.channel.purge(limit=5)
    embed = discord.Embed(
            title="Verification Requirement",
            description="`Age role`  and `Gender role` Needed for Verification",
            color=discord.Colour(0x2f3136)
        )
    await ctx.send(embed=embed)
    await ctx.send(file=discord.File(bot_configs.verfi_image()),view=StartVerify(bot))


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
    await load()
    await bot.start(os.getenv('token'))
    
    

asyncio.run(main())