from datetime import datetime
#datetime.utcnow().strftime("%d-%m-%Y")

import discord
from discord.ui import Button, View
from src.core.config_parser import BotConfigs

from src.btns.selfie_decline_btn import DeclineBtn as dec

bot_configs = BotConfigs()

# DB 
from ..model import dbinput

from src.model import queries

user_in_db = queries.verifiedque()

def dbinputfun(user, roleid):
    if user_in_db.get_user(user.id):
        user_in_db.update("selfie_verified_g", f"{roleid}", user.id)
        user_in_db.update("selfie_verification_date", datetime.utcnow().strftime("%d-%m-%Y"), user.id)

    else:
        dbinput.verify_data(str(user), str(user.id), age_verified= 0, age_verified_g = None, selfie_verified = 1, selfie_verified_g = f"{roleid}", age_verification_date = None,  selfie_verification_date = datetime.utcnow().strftime("%d-%m-%Y"))


class SelfieVerify(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label='Accept', style=discord.ButtonStyle.green, custom_id='accept')
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):

        #selfie verified role
        roleObj = discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('self_ver'))

        embeds = interaction.message.embeds[0].to_dict()
        
        user_id = embeds['footer']['text']
        print("user to give role id", user_id)

        user = await interaction.guild.fetch_member(user_id)

        #selfie_verfy_gender_roles
        self.self_ver_m =  discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('self_ver_m'))
        self.self_ver_f=  discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('self_ver'))
        self.self_ver_nb =  discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('self_ver'))
        self.self_ver_gf =  discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('self_ver'))
        self.self_ver_t_ftm = discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('self_ver'))
        self.self_ver_t_mtf = discord.utils.get(interaction.guild.roles, id=bot_configs.verfy_roles('self_ver'))


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

        #dbinput.verify_data(user, user.id, age_verified= 0, age_verified_g = None, selfie_verified = 1, selfie_verified_g = f"", age_verification_date = None ,  selfie_verification_date = datetime.utcnow().strftime("%d-%m-%Y"))

        # add selfie verified role
        if self.role_male in user.roles:

            dbinputfun(user,self.self_ver_m.id)
            await user.add_roles(self.self_ver_m)

            

        elif self.role_female in user.roles:
            await user.add_roles(self.self_ver_f)

        elif self.role_non_binary in user.roles:
            await user.add_roles(self.self_ver_nb)

        elif self.role_genderfluid in user.roles:
            await user.add_roles(self.self_ver_gf)

        elif self.role_t_ftm in user.roles:
            await user.add_roles(self.self_ver_t_ftm)

        elif self.role_t_mtf in user.roles:
            await user.add_roles(self.self_ver_t_mtf)



        

        # add selfie verified role
        await user.add_roles(roleObj)
        

        chn = self.bot.get_channel(bot_configs.channel_id('verification_log'))
        embed_log = discord.Embed(description=f"Verification of <@{user.id}> **ID**: {user.id} got handled by <@{interaction.user.id}> **ID**: {interaction.user.id} ", 
                                  color=discord.Color.blue() )
        embed_log.set_author(name=f"{interaction.guild.name} Verification", icon_url=f"{interaction.guild.icon.url}")
        embed_log.add_field(name="Verification Button",value="Accepted", inline=False)
        
        await chn.send(embed=embed_log)
         

        await interaction.response.defer()
        await user.send("verification accepted")
        await interaction.delete_original_response()
        await interaction.channel.purge(limit=1)

    


    #Decline
    @discord.ui.button(label='decline', style=discord.ButtonStyle.red, custom_id='decline')
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        """
        embeds = interaction.message.embeds[0].to_dict()
        user_id = embeds['footer']['text']

        user = await interaction.guild.fetch_member(user_id)
        """

        await interaction.response.edit_message(view=dec(self.bot))