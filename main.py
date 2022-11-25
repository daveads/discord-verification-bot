import asyncio
from discord.ext import commands
import discord

from src.core.startverify  import StartVerify
from src.core.bot   import VerificationBot
from src.core.config_parser import BotConfigs

bot = VerificationBot()
bot_configs = BotConfigs()

@bot.command()
@commands.is_owner()
async def prepare(ctx: commands.Context):

    print(bot_configs.verfi_image())

    await ctx.send(file=discord.File(bot_configs.verfi_image()), view=StartVerify(bot))


async def main():
    await bot.start('MTAzMzQwMTI5NTc2MTA2MDAwMg.Gr5jg7.lrFdyxe5ohlJZkTkRMkO6pLqsplQ0Txye6Fw4E')
    
    

asyncio.run(main())