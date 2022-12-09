from multiprocessing import Value
import discord
from src.core.config_parser import BotConfigs

from src.btns.decline_btn import DeclineBtn as dec
bot_configs = BotConfigs()

class AgeVerify(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label='Accept', style=discord.ButtonStyle.green, custom_id='accepta')
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):

        roleObj = discord.utils.get(interaction.guild.roles, id=bot_configs.roles("age_ver"))

        embeds = interaction.message.embeds[0].to_dict()
        
        user_id = embeds['footer']['text']
        print("user to give role id", user_id)

        user = await interaction.guild.fetch_member(user_id)
        
        # add the verifiy role
        await user.add_roles(roleObj)
      
        chn = self.bot.get_channel(1034399992632324107)
        embed_log = discord.Embed(description=f"Verification of <@{user.id}> **ID**: {user.id} got handled by <@{interaction.user.id}> **ID**: {interaction.user.id} ", 
                                  color=discord.Color.blue() )
        embed_log.set_author(name=f"{interaction.guild.name} Verification", icon_url=f"{interaction.guild.icon.url}")
        embed_log.add_field(name="Verification Button",value="Accepted", inline=False)
        
        await chn.send(embed=embed_log)
         

        await user.send("verification accepted ***")
        await interaction.response.defer()
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