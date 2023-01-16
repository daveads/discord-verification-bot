from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    #@commands.guild_only()
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        print(guild.name)
        print(member.id)
        
        


async def setup(bot):
    await bot.add_cog(Events(bot))