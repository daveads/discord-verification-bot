import discord

async def embed_log(bot, interaction, user, reason):

   chn = bot.get_channel(1034399992632324107)
   embed_log = discord.Embed(description=f"Verification of <@{user.id}> **ID**: {user.id} got handled by <@{interaction.user.id}> **ID**: {interaction.user.id} ", 
                            color=discord.Color.blue() )
   embed_log.set_author(name=f"{interaction.guild.name} Verification", icon_url=f"{interaction.guild.icon.url}")
   embed_log.add_field(name="Verification Button",value="Declined", inline=False)   
   embed_log.add_field(name="Deny Reason", value=f"{reason}") 

   await interaction.response.defer()  
   await chn.send(embed=embed_log)


   await interaction.delete_original_response()
   await interaction.channel.purge(limit=1)

class custom_decline(discord.ui.Modal, title='decline message'):

    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.add_item(
        discord.ui.TextInput(
        label='Reply',
        placeholder='custom reply...',
        custom_id = "custom_decline"
    ))



    async def on_submit(self, interaction: discord.Interaction):
        embeds = interaction.message.embeds[0].to_dict()
        user_id = embeds['footer']['text']

        user = await interaction.guild.fetch_member(user_id)
        
        await user.send(f"{self.children[0].value}")
        await embed_log(self.bot, interaction, user, self.children[0].value)