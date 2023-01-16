import discord
from discord.ext import commands
from src.model import queries

user_in_db = queries.verifiedque()

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.dic_key = ['id','username','user_id', "age_verified", "age_verified_g", "selfie_verified", "selfie_verified_g", "age_verification_date", "selfie_verification_date"]

    #@commands.guild_only()
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        print(guild.name)
        print(member.id)
        
        if user_in_db.get_user(member.id):
                
            user_d = user_in_db.get_user(member.id)
            user_data ={}

            for i in range(len(self.dic_key)):
                user_data[self.dic_key[i]] = user_d[i]

            print(user_data)


            if user_data["age_verified"]:
                ageverg = discord.utils.get(guild.roles, id=int(user_data["age_verified_g"]))

                member.add_roles(ageverg)
                #member.add_roles(agev)


            if user_data["selfie_verified"]:
                selfieg = discord.utils.get(guild.roles, id=int(user_data["selfie_verified_g"]))
                
                member.add_role(selfieg)
                #membrer.add_roles(selfiev)

        else:
            print("<<<<< USER has no roles >>>>>")
            roleObj = discord.utils.get(guild.roles, id=1046031060481360002)

            await member.add_roles(roleObj)

        
        


async def setup(bot):
    await bot.add_cog(Events(bot))