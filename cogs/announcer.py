import discord
from discord.ext import commands

from modal.announce_modal import announce
class announcer(commands.Cog):
     def __init__(self, bot):
        self.bot = bot
 

    
def setup(bot):
    bot.add_cog(announcer(bot))
    