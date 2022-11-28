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
    
        await user.send("verification accepted")
        await interaction.response.defer()
        await interaction.delete_original_response()
        await interaction.channel.purge(limit=1)

    


    #Decline
    @discord.ui.button(label='decline', style=discord.ButtonStyle.red, custom_id='declinea')
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        """
        embeds = interaction.message.embeds[0].to_dict()
        user_id = embeds['footer']['text']

        user = await interaction.guild.fetch_member(user_id)
        """

        await interaction.response.edit_message(view=dec())