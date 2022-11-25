import discord

class UserVerify(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)

        self.bot = bot

    @discord.ui.button(label='Accept', style=discord.ButtonStyle.green, custom_id='accept')
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):


        embeds = interaction.message.embeds[0].to_dict()
        
        user_id = embeds['footer']['text']
        print("user to give role id", user_id)

        self.user = await interaction.guild.fetch_member(user_id)
        await self.user.send("verification accepted")

        await interaction.response.defer()
        await interaction.delete_original_response()
        await interaction.channel.purge(limit=1)

        
    

    @discord.ui.button(label='decline', style=discord.ButtonStyle.red, custom_id='decline')
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
 
        await interaction.response.send_message("declined")

        
