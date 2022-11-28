import discord
from src.btns.custom_decline_btn import custom_decline
#from src.core.userverify import UserVerify
#from ..core.userverify import UserVerify as ver


async def inter_func(interaction):
      await interaction.response.defer()
      await interaction.delete_original_response()
      await interaction.channel.purge(limit=1)

async def user_obj(interaction):
   embeds = interaction.message.embeds[0].to_dict()
   user_id = embeds['footer']['text']
   user = await interaction.guild.fetch_member(user_id)
   return user
    

class DeclineBtn(discord.ui.View):

     def __init__(self):
        super().__init__(timeout=None)
    
     @discord.ui.button(label='Not enough Information', style=discord.ButtonStyle.grey, custom_id='1' , row=1)
     async def nei(self, interaction: discord.Interaction, button: discord.ui.Button):
      user = await user_obj(interaction)
      await user.send("Not enough Information")
      await inter_func(interaction)


     @discord.ui.button(label='Face not clearly shown', style=discord.ButtonStyle.grey, custom_id='2', row=1)
     async def call_back(self, interaction: discord.Interaction, button: discord.ui.Button):
      user = await user_obj(interaction)
      await user.send("Face not clearly shown")
      await inter_func(interaction)


     
     @discord.ui.button(label='Ask to retry', style=discord.ButtonStyle.grey, custom_id='3', row=1)
     async def atr(self, interaction: discord.Interaction, button: discord.ui.Button):
      user = await user_obj(interaction)
      await user.send("retry verification")
      await inter_func(interaction)



     @discord.ui.button(label='Read Description and Try again', style=discord.ButtonStyle.grey, custom_id='4', row=2)
     async def rdta(self, interaction: discord.Interaction, button: discord.ui.Button):
      user = await user_obj(interaction)
      await user.send("Read Description and Try again")
      await inter_func(interaction)


     @discord.ui.button(label='Custom Reason', style=discord.ButtonStyle.grey, custom_id='5', row=2)
     async def cr(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.send_modal(custom_decline())
      await inter_func(interaction)


     @discord.ui.button(label='Go Back', style=discord.ButtonStyle.red, custom_id='6', row=3)
     async def go_back(self, interaction: discord.Interaction, button: discord.ui.Button):
      #await interaction.response.edit_message(view=None)
      await interaction.response.edit_message(view=self)