import discord
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
            
            """
            IF selfie_verified:
                add(selfie)
                add(selfie_g)
        
            IF age_verified:
                add(agev)
                add(agevg)
            """

        else:
            print("<<<<< USER has no roles >>>>>")
            roleObj = discord.utils.get(guild.roles, id=1046031060481360002)

            await member.add_roles(roleObj)

        
        


async def setup(bot):
    await bot.add_cog(Events(bot))