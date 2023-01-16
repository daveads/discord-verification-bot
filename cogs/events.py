from xml.etree.ElementTree import fromstring
from discord.ext import commands
from src.model import queries

user_in_db = queries.verifiedque()

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    #@commands.guild_only()
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        print(guild.name)
        print(member.id)

        if user_in_db.get_user(member.id):
            print("<<<<< USER IS IN DB >>>>>")

        else:
            print("<<<<< USER has no roles >>>>>")

        
        


async def setup(bot):
    await bot.add_cog(Events(bot))