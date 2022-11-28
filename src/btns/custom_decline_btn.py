import discord

class custom_decline(discord.ui.Modal, title='cus_decline'):

    def __init__(self):
        super().__init__(timeout=None)
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
        await interaction.response.defer()
        await user.send(f"{self.children[0].value}")
        await interaction.delete_original_response()
        await interaction.channel.purge(limit=1)

