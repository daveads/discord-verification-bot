import asyncio
import discord
from discord.ui import Button, View


from src.core.selfieverify import SelfieVerify
from src.core.ageverify    import AgeVerify

from src.core.config_parser import BotConfigs

bot_configs = BotConfigs()

async def get_element(array):
    element = None
    for i in range(len(array)):
        if array[i] == True:
            element = i
            #print(i)
               
    return element


async def user_reply(user, bot, chh, channel_created):
    def check(message):
        return message.author == user and bool(message.attachments)
           
           
    try:
        resp = await bot.wait_for('message', check=check , timeout=65.0)


    except  asyncio.TimeoutError:
        await chh.send(f"Time out {user.mention}")
        await asyncio.sleep(20)
        await channel_created.delete()
           
    
    d = str(resp.attachments[0])
    format = ['png', 'jpg', 'jpeg', 'heic']

    if d[-3:] in format:     
        return resp.attachments[0]


class VerifyBtn(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.user_chan = False
        self.format = ['png', 'jpg', 'jpeg', 'heic']

        self.face = ['😉', '😗', '😱' , '😛', '😜', ]
        self.hand = ['🖐️', '✋', '👌', '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👍', '👎']


        import random

        self.emoji =f"{random.choice(self.face)} {random.choice(self.hand)}"



    @discord.ui.button(label='Selfie Verifications', style=discord.ButtonStyle.grey, custom_id='emojiprs')
    async def emoji(self, interaction: discord.Interaction, button: discord.ui.Button):
       

       self.user = await interaction.guild.fetch_member(interaction.user.id)
       self.self_ver_role_obj = discord.utils.get(interaction.guild.roles, id=bot_configs.roles("self_ver"))


       #gender roles
       self.role_male =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("male")) 
       self.role_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("female"))
       self.role_trans_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("trans_female"))
       self.role_non_binary =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("non_binary"))
       self.role_agender =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("agender"))
       self.role_bigender = discord.utils.get(interaction.guild.roles, id=bot_configs.roles("bigender"))
       self.role_genderfluid = discord.utils.get(interaction.guild.roles, id=bot_configs.roles("genderfluid"))
       

       #age roles 
       self.a18_22 = discord.utils.get(interaction.guild.roles, id=bot_configs.roles('18-22')) 
       self.a23_27 = discord.utils.get(interaction.guild.roles, id=bot_configs.roles('23-27')) 
       self.a28_30 = discord.utils.get(interaction.guild.roles, id=bot_configs.roles('28-30+')) 

       gender_roles = [self.role_male, self.role_female, self.role_trans_female, self.role_non_binary, self.role_agender, self.role_bigender, self.role_genderfluid]
       
       age_roles = [self.a18_22, self.a23_27, self.a28_30]
       
       import numpy as np
       gender_check = np.isin(gender_roles, self.user.roles)
       age_check = np.isin(age_roles, self.user.roles)

 
       """
       ele = None
       for i in range(len(age_check)):
        if age_check[i] == True:
            ele = i

       print(ele)
       print("age is between", age_roles[ele])
       """
       

       age_get = await get_element(age_check)
       gender_get = await get_element(gender_check)


       if True in gender_check:
        if True in age_check:
            if self.self_ver_role_obj in self.user.roles:
                button.disabled = True
                button.style = discord.ButtonStyle.green
                button.label = "Already Verified"
                await interaction.user.send("Already Verified")
                await interaction.response.edit_message(view=self)


            else:
                #print(self.user.id)
                #print("checking", self.user)
       
                guild = interaction.guild

                admin_role = guild.get_role(1034410474189623347)

                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    admin_role: discord.PermissionOverwrite(view_channel=True),
                    guild.me: discord.PermissionOverwrite(view_channel=True, read_messages=True),
                    interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages = True, attach_files = True) 
                }
       
                category = discord.utils.get(interaction.guild.categories, id=1050013059063762984)
       
                """
                #print(interaction.guild.text_channels)
                for text_channel in interaction.message.guild.text_channels:
                print(text_channel.name)
           
                """
       
                channel_name = f"selfie_ver-{interaction.user.id}"

      
                userverify_channels = []
       
                for i in category.channels:
                    userverify_channels.append(i.name)
       
       

                #checks if there is any pending channel
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
           
       
       
                    #THE CHANNEL
                    chh = discord.utils.get(guild.channels, name=channel_name)
                    # interaction.user.mention
                    await chh.send(interaction.user.mention)
           
                    
                    embed_first=discord.Embed(color=discord.Color.blue())
                    #embed_first.set_thumbnail(url=f"{interaction.user.avatar}")
                    embed_first.set_author(name=f"{interaction.guild.name} Verification", icon_url=f"{interaction.guild.icon.url}")
                    embed_first.add_field(name="First picture", value=f"make a selfie of you mimicing the following combination of emoji {self.emoji} \n\n  **UPLOADED FILE SHOULD ONLY BE PICTURES**", inline=True)

                
                    embed_wanning = discord.Embed(color=discord.Color.blue())
                    embed_wanning.set_author(name=f"{interaction.guild.name} Verification", icon_url=f"{interaction.guild.icon.url}")
                    embed_wanning.add_field(name="------------------------",value="Waiting for image  \n\n  **Timeout in 5 minutes**", inline=True)
                    

                    await chh.send(embed=embed_first)
                    await chh.send(embed=embed_wanning)

                    await asyncio.sleep(2)

                    """          
                    def check(message):
                        return message.author == self.user and bool(message.attachments)
           
           
                    try:
                        resp = await self.bot.wait_for('message', check=check , timeout=65.0)


                    except  asyncio.TimeoutError:
                        await chh.send(f"Time out {self.user.mention}")
                        await asyncio.sleep(20)
                        await channel_created.delete()
           
                   
                    #await resp.attachments[0].save(f'{user.id}-0.jpg')
           
                    image = resp.attachments[0]
           
                    """

                    image1 = await user_reply(self.user, self.bot, chh, channel_created)
                    
                    
                    # Needs refactory
                    while(True):

                        if image1 == None:
                            await chh.send("uploaded file can only be a image file")
                            image1 = await user_reply(self.user, self.bot, chh, channel_created)
                        
                        elif image1 !=None:
                            break
                    

                    
                    # SELFIE-VERIFICATION CHANNEL
                    selfie_verf = discord.utils.get(guild.channels, id=bot_configs.channel_id("self_verification"))
                    
                    # First Embed 
                    embed1=discord.Embed(title=f"{self.user} Selfie verification",  description="checking", color=discord.Color.blue())
                    embed1.add_field(name="FIRST IMAGE", value=f"T", inline=True)
                    embed1.add_field(name="Gender", value=f"{gender_roles[gender_get]}", inline=True)
                    embed1.add_field(name="Age", value=f"{age_roles[age_get]}", inline=True)
                    embed1.set_image(url=image1)
                    embed1.set_footer(text=f"{self.user.id}")
           
           
                    

                    
                    if (image1):
                        embed_second=discord.Embed(color=discord.Color.blue())
                        #embed_first.set_thumbnail(url=f"{interaction.user.avatar}")
                        embed_second.set_author(name=f"{interaction.guild.name} Verification", icon_url=f"{interaction.guild.icon.url}")
                        embed_second.add_field(name="Second picture", value=f"make a selfie of you mimicing the following combination of emoji {self.emoji} \n\n  **UPLOADED FILE SHOULD ONLY BE PICTURES**", inline=True)

                        await chh.send(embed=embed_second)
                        image2 = await user_reply(self.user, self.bot, chh, channel_created)


                    # Needs refactory
                    while(True):

                        if image2 == None:
                            await chh.send("uploaded file can only be a image file")
                            image2 = await user_reply(self.user, self.bot, chh, channel_created)
                        
                        elif image2 !=None:
                            break
                    
                    #SECOND IMAGE EMBED 
                    embed2=discord.Embed(title=f"{self.user} Selfie verification",  description="checking", color=discord.Color.blue())
                    embed2.add_field(name="SECOND IMAGE", value=f"T", inline=True)
                    embed2.add_field(name="Gender", value=f"{gender_roles[gender_get]}", inline=True)
                    embed2.add_field(name="Age", value=f"{age_roles[age_get]}", inline=True)
                    embed2.set_image(url=image2)
                    embed2.set_footer(text=f"{self.user.id}")
           
                    await selfie_verf.send(embed=embed1)
           
                    await selfie_verf.send(embed=embed2, view=SelfieVerify(self.bot))
           
                    print(channel_created.id)
        
                    if (image2):
                        await asyncio.sleep(10)
                        await channel_created.delete()

        else:
            await interaction.response.defer()
            await interaction.user.send("you are missing age role")
         

       else:
        await interaction.response.defer()
        await interaction.user.send("you are missing gender role")
        

    
    
    
    
    
    
    
    
    
    
    
    
    @discord.ui.button(label='Age Verifications', style=discord.ButtonStyle.grey, custom_id='age_verf')
    async def age_verf(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        """
        Do something 
        """
        self.user = await interaction.guild.fetch_member(interaction.user.id)
        self.age_ver_role_obj = discord.utils.get(interaction.guild.roles, id=bot_configs.roles("age_ver"))

        #gender roles
        self.role_male =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("male")) 
        self.role_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("female"))
        self.role_trans_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("trans_female"))
        self.role_non_binary =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("non_binary"))
        self.role_agender =  discord.utils.get(interaction.guild.roles, id=bot_configs.roles("agender"))
        self.role_bigender = discord.utils.get(interaction.guild.roles, id=bot_configs.roles("bigender"))
        self.role_genderfluid = discord.utils.get(interaction.guild.roles, id=bot_configs.roles("genderfluid"))
       
        #age roles 
        self.a18_22 = discord.utils.get(interaction.guild.roles, id=bot_configs.roles('18-22')) 
        self.a23_27 = discord.utils.get(interaction.guild.roles, id=bot_configs.roles('23-27')) 
        self.a28_30 = discord.utils.get(interaction.guild.roles, id=bot_configs.roles('28-30+')) 

        gender_roles = [self.role_male, self.role_female, self.role_trans_female, self.role_non_binary, self.role_agender, self.role_bigender, self.role_genderfluid]
       
        age_roles = [self.a18_22, self.a23_27, self.a28_30]
       
        import numpy as np
        gender_check = np.isin(gender_roles, self.user.roles)

        age_check = np.isin(age_roles, self.user.roles)


        age_get = await get_element(age_check)
        gender_get = await get_element(gender_check)

        if True in gender_check:
            if True in age_check:
                if self.age_ver_role_obj in self.user.roles:
                    button.disabled = True
                    button.style = discord.ButtonStyle.green
                    button.label = "Already Verified"
                    await interaction.user.send("Already Verified")
                    await interaction.response.edit_message(view=self)

                else:

                    guild = interaction.guild

                    admin_role = guild.get_role(1034410474189623347)

                    overwrites = {
                        guild.default_role: discord.PermissionOverwrite(view_channel=False),
                        admin_role: discord.PermissionOverwrite(view_channel=True),
                        guild.me: discord.PermissionOverwrite(view_channel=True, read_messages=True),
                        interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages = True, attach_files = True) 
                    }
       

                    category = discord.utils.get(interaction.guild.categories, id=1050013059063762984)
       
                    channel_name = f"age_ver-{interaction.user.id}"

      
                    userverify_channels = []
       
                    for i in category.channels:
                        userverify_channels.append(i.name)
       
 
                    #checks if there is any pending channel
                    for i in userverify_channels:
                        if str(self.user.id) in i:
                            self.user_chan = True

                    if self.user_chan:        
                        await interaction.response.edit_message(content="verification pending", view=None) 

                    else:
                        await guild.create_text_channel(channel_name,  category=category, overwrites=overwrites)
           
                        channel_created = discord.utils.get(guild.channels, name=channel_name)
                        button = Button(label="Go to Channel", url=f"https://discord.com/channels/{interaction.guild.id}/{channel_created.id}" ,  style=discord.ButtonStyle.grey)
                        view = View()
                        view.add_item(button)
                        await interaction.response.edit_message(content="Verification started click the button below to get to the channel! ", view=view)


                        #THE CHANNEL
                        chh = discord.utils.get(guild.channels, name=channel_name)
                        # interaction.user.mention
                        await chh.send(interaction.user.mention)


                        embed_first=discord.Embed(color=discord.Color.blue())
                        #embed_first.set_thumbnail(url=f"{interaction.user.avatar}")
                        embed_first.set_author(name=f"{interaction.guild.name} Age Verification", icon_url=f"{interaction.guild.icon.url}")
                        embed_first.add_field(name="First picture", value=f"make a selfie of you holding your id card** \n\n  **UPLOADED FILE SHOULD ONLY BE PICTURES**", inline=True)

                
                        embed_wanning = discord.Embed(color=discord.Color.blue())
                        embed_wanning.set_author(name=f"{interaction.guild.name} Verification", icon_url=f"{interaction.guild.icon.url}")
                        embed_wanning.add_field(name="------------------------",value="Waiting for image  \n\n  **Timeout in 5 minutes**", inline=True)
                    

                        await chh.send(embed=embed_first)
                        await chh.send(embed=embed_wanning)

                        await asyncio.sleep(2)


                        image1 = await user_reply(self.user, self.bot, chh, channel_created)

                        while(True):
                            if image1 == None:
                                await chh.send("uploaded file can only be a image file")
                                image1 = await user_reply(self.user, self.bot, chh, channel_created)
                        
                            elif image1 !=None:
                                break

                    
                        # AGE-VERIFICATION CHANNEL
                        age_verf = discord.utils.get(guild.channels, id=bot_configs.channel_id("age_Verification"))

                        # First Embed 
                        embed1=discord.Embed(title=f"{self.user} Age verification",  description="checking", color=discord.Color.blue())
                        embed1.add_field(name="FIRST IMAGE", value=f"T", inline=True)
                        embed1.add_field(name="Gender", value=f"{gender_roles[gender_get]}", inline=True)
                        embed1.add_field(name="Age", value=f"{age_roles[age_get]}", inline=True)
                        embed1.set_image(url=image1)
                        embed1.set_footer(text=f"{self.user.id}")


                        if (image1):
                            embed_second=discord.Embed(color=discord.Color.blue())
                            #embed_first.set_thumbnail(url=f"{interaction.user.avatar}")
                            embed_second.set_author(name=f"{interaction.guild.name} Verification", icon_url=f"{interaction.guild.icon.url}")
                            embed_second.add_field(name="Second picture", value=f"Take a clear picture of the ID CARD \n\n  **UPLOADED FILE SHOULD ONLY BE PICTURES**", inline=True)

                            await chh.send(embed=embed_second)
                            image2 = await user_reply(self.user, self.bot, chh, channel_created)


                        # Needs refactory
                        while(True):
                            if image2 == None:
                                await chh.send("uploaded file can only be a image file")
                                image2 = await user_reply(self.user, self.bot, chh, channel_created)
                        
                            elif image2 !=None:
                                break
                    

                        #SECOND IMAGE EMBED 
                        embed2=discord.Embed(title=f"{self.user} Selfie verification",  description="checking", color=discord.Color.blue())
                        embed2.add_field(name="SECOND IMAGE", value=f"T", inline=True)
                        embed2.add_field(name="Gender", value=f"{gender_roles[gender_get]}", inline=True)
                        embed2.add_field(name="Age", value=f"{age_roles[age_get]}", inline=True)
                        embed2.set_image(url=image2)
                        embed2.set_footer(text=f"{self.user.id}")
           
                        await age_verf.send(embed=embed1)
           
                        await age_verf.send(embed=embed2, view=AgeVerify(self.bot))
           
                        if (image2):
                            await asyncio.sleep(10)
                            await channel_created.delete()
           
           
                    










            else:
                await interaction.response.defer()
                await interaction.user.send("you are missing age role")

        else:
            await interaction.response.defer()
            await interaction.user.send("you are missing gender role")
