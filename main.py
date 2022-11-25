import asyncio
from discord.ext import commands
import discord

from src.core.startverify  import StartVerify
from src.core.bot   import VerificationBot

bot = VerificationBot()

@bot.command()
@commands.is_owner()
async def prepare(ctx: commands.Context):
    #startverify = StartVerify()
    #await startverify.getobj(bot)
    
    await ctx.send(file=discord.File('src/img/ID-Verification-post.png'), view=StartVerify(bot))

async def main():
    await bot.start('MTAzMzQwMTI5NTc2MTA2MDAwMg.Gr5jg7.lrFdyxe5ohlJZkTkRMkO6pLqsplQ0Txye6Fw4E')
    

asyncio.run(main())