from datetime import datetime
import discord
from src.core.config_parser import BotConfigs

from src.btns.age_decline_btn import AgeDeclineBtn as dec
bot_configs = BotConfigs()


# DB 
from ..model import dbinput

from src.model import queries

user_in_db = queries.verifiedque()

async def get_element(array):
    element = None
    for i in range(len(array)):
        if array[i] == True:
            element = i
            #print(i)
               
    return element


def dbinputfun(user, roleid, gender, age):
    if user_in_db.get_user(user.id):
        user_in_db.update("age_verified_g", f"{roleid}", user.id)
        user_in_db.update("age_verified", 1, user.id)
        user_in_db.update("age_verification_date", datetime.utcnow().strftime("%d-%m-%Y"), user.id)

    else:
        dbinput.verify_data(str(user), str(user.id), gender=gender, age =age, age_verified= 1, age_verified_g = f"{roleid}", selfie_verified = 0, selfie_verified_g = None, age_verification_date = datetime.utcnow().strftime("%d-%m-%Y"),  selfie_verification_date = None)

#AGEVERIFY
class AgeVerify(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label='Accept', style=discord.ButtonStyle.green, custom_id='accepta')
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):

        roleObj = discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('age_ver'))

        embeds = interaction.message.embeds[0].to_dict()
        
        user_id = embeds['footer']['text']
        print("user to give role id", user_id)

        user = await interaction.guild.fetch_member(user_id)

        #selfie_verfy_gender_roles
        self.age_ver_m =  discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('age_ver_m'))
        self.age_ver_f=  discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('age_ver_f'))
        self.age_ver_nb =  discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('age_ver_nb'))
        self.age_ver_gf =  discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('age_ver_gf'))
        self.age_ver_t_ftm = discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('age_ver_t_ftm'))
        self.age_ver_t_mtf = discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('age_ver_t_mtf'))


        #gender roles
        self.role_male =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender('male')) 
        self.role_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("female"))
        self.role_trans_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("trans_female"))
        self.role_non_binary =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("non_binary"))
        self.role_agender =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("agender"))
        self.role_bigender = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("bigender"))
        self.role_genderfluid = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("genderfluid"))
        self.role_t_ftm = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("t_ftm"))
        self.role_t_mtf = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("t_mtf"))

        self.a18_22 = discord.utils.get(interaction.guild.roles, id=bot_configs.age_roles('18-22')) 
        self.a23_27 = discord.utils.get(interaction.guild.roles, id=bot_configs.age_roles('23-27')) 
        self.a28_30 = discord.utils.get(interaction.guild.roles, id=bot_configs.age_roles('28-30+'))

        gender_roles = [self.role_male, self.role_female, self.role_trans_female, self.role_non_binary, self.role_agender, self.role_bigender, self.role_genderfluid, self.role_t_ftm, self.role_t_mtf]
        age_roles = [self.a18_22, self.a23_27, self.a28_30]
        
        import numpy as np
        gender_check = np.isin(gender_roles, user.roles)
        age_check = np.isin(age_roles, user.roles)


        age_get = await get_element(age_check)
        gender_get = await get_element(gender_check)
        
        #print("gender", gender_roles[gender_get].id)
        #print("age", age_roles[age_get].id)

        gender = gender_roles[gender_get].id
        age = age_roles[age_get].id


        # add selfie verified role
        if self.role_male in user.roles:

            dbinputfun(user,self.age_ver_m.id, gender, age)
            await user.add_roles(self.age_ver_m)

            

        elif self.role_female in user.roles:
            await user.add_roles(self.age_ver_f)

        elif self.role_non_binary in user.roles:
            await user.add_roles(self.age_ver_nb)

        elif self.role_genderfluid in user.roles:
            await user.add_roles(self.age_ver_gf)

        elif self.role_t_ftm in user.roles:
            await user.add_roles(self.age_ver_t_ftm)

        elif self.role_t_mtf in user.roles:
            await user.add_roles(self.age_ver_t_mtf)

        # add the verifiy role
        await user.add_roles(roleObj)
      
        chn = self.bot.get_channel(bot_configs.channel_id('verification_log')) 

        embed_log = discord.Embed(description=f"Verification of <@{user.id}> **ID**: {user.id} got handled by <@{interaction.user.id}> **ID**: {interaction.user.id} ", 
                                  color=discord.Color.blue() )
        embed_log.set_author(name=f"{interaction.guild.name} Verification", icon_url=f"{interaction.guild.icon.url}")
        embed_log.add_field(name="Verification Button",value="Accepted", inline=False)
        
        await chn.send(embed=embed_log)
         

        await interaction.response.defer()
        await user.send("verification accepted ***")
        await interaction.delete_original_response()
        await interaction.channel.purge(limit=1)

        #chn = discord.utils.get(interaction.guild, id=1034399992632324107)

        #await chn.send("hello")
        


    #Decline
    @discord.ui.button(label='decline', style=discord.ButtonStyle.red, custom_id='declinea')
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        """
        embeds = interaction.message.embeds[0].to_dict()
        user_id = embeds['footer']['text']

        user = await interaction.guild.fetch_member(user_id)
        """

        await interaction.response.edit_message(view=dec(self.bot))