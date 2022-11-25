import asyncio
import discord
from discord.ui import Button, View

from src.core.userverify import UserVerify


class VerifyBtn(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.user_chan = False
        self.format = ['png', 'jpg', 'jpeg', 'heic']
        
    @discord.ui.button(label='Selfie Verifications', style=discord.ButtonStyle.grey, custom_id='emojiprs')
    async def emoji(self, interaction: discord.Interaction, button: discord.ui.Button):
       
       #user = await self.bot.fetch_user(interaction.user.id)
       self.user = await interaction.guild.fetch_member(interaction.user.id)
       print(self.user.id)
       print("checking", self.user)
       
       guild = interaction.guild

       admin_role = guild.get_role(1034410474189623347)

       overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        admin_role: discord.PermissionOverwrite(view_channel=True),
        guild.me: discord.PermissionOverwrite(view_channel=True, read_messages=True),
        interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages = True, attach_files = True) 
    }
       
       category = discord.utils.get(interaction.guild.categories, id=1034398945083916338)
       
       """
       #print(interaction.guild.text_channels)
       for text_channel in interaction.message.guild.text_channels:
        print(text_channel.name)
           
       """
       
       channel_name = f"emoji-{interaction.user.id}"

      
       userverify_channels = []
       
       for i in category.channels:
              userverify_channels.append(i.name)
       
       
       print(userverify_channels)
    
       for i in userverify_channels:
  
           if str(self.user.id) in i:
               self.user_chan = True
               
               
       print(self.user_chan)
       
       if self.user_chan:        
           await interaction.response.edit_message(content="verification pending", view=None)  
                 
       else:
           
           await guild.create_text_channel(channel_name,  category=category, overwrites=overwrites)
           
           channel_created = discord.utils.get(guild.channels, name=channel_name)
           button = Button(label="Go to Channel", url=f"https://discord.com/channels/{interaction.guild.id}/{channel_created.id}" ,  style=discord.ButtonStyle.grey)
           view = View()
           view.add_item(button)
           await interaction.response.edit_message(content="Verification started click the button below to get to the channel! ", view=view)
           
       
       
           # THE CHANNEL
           chh = discord.utils.get(guild.channels, name=channel_name)
           # interaction.user.mention
           await chh.send(interaction.user.mention)
           
           print(self.user)
           def check(message):
               return message.author == self.user and bool(message.attachments)
           
           
           await chh.send('upload your picture')
           await asyncio.sleep(2)
           
           try:
               resp = await self.bot.wait_for('message', check=check , timeout=65.0)


           except  asyncio.TimeoutError:
               await chh.send(f"Time out {self.user.mention}")
               await asyncio.sleep(20)
               await channel_created.delete()
           
                   
           #await resp.attachments[0].save(f'{user.id}-0.jpg')
           
           image = resp.attachments[0]
           
           # SELFIE-VERIFICATION 
           selfie_verf = discord.utils.get(guild.channels, id=1034398479759450172)
           
           #await selfie_chh.send(user)
           embed=discord.Embed(title=f"{self.user} Selfie verification",  description="checking", color=discord.Color.blue())
           embed.add_field(name="FIRST IMAGE", value=f"T", inline=True)
           embed.add_field(name="Gender", value=f"Male", inline=True)
           embed.add_field(name="Age", value=f"24", inline=True)
           embed.set_image(url=image)
           embed.set_footer(text=f"{self.user.id}")
           
           
           await selfie_verf.send(embed=embed)
           
           await selfie_verf.send(embed=embed, view=UserVerify(self.bot))
           
           #await self.bot.add_view(UserVerify(self.user))

           print(channel_created.id)
           
           if (await chh.send(image)):
               
               await asyncio.sleep(10)
               await channel_created.delete()
       



    
    
    
    
    
    
    
    
    
    
    
    
    @discord.ui.button(label='Age Verifications', style=discord.ButtonStyle.grey, custom_id='videoprs', disabled = True)
    async def video(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        """
        Do something 
        """
       
        button = Button(label="Go to Channel", style=discord.ButtonStyle.grey)
        view = View()
        view.add_item(button)
        await interaction.response.edit_message(content="Verification started click the button below to get to the channel! ", view=view)


    async def getuserobj(self):
        return self.user