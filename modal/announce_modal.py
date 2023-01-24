import discord

from core.config_parser import BotConfigs
botconfig = BotConfigs()

class announce(discord.ui.Modal):
     def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print(args)
        print(kwargs)

        self.add_item(discord.ui.InputText(label="Title", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="announcement", style=discord.InputTextStyle.long))



     async def callback(self, interaction: discord.Interaction):
        
        announce_chn = discord.utils.get(interaction.guild.channels, id=botconfig.channel_id("announcement_chnn"))

        embed = discord.Embed(title="Profile Bot Feature Annoucement", description=f"Title : `{self.children[0].value}` " , color=discord.Colour(0x2f3136),)

        embed.add_field(name="INFO", value=self.children[1].value)
        embed.set_footer(text="From @daveads")

        await announce_chn.send(embed=embed)
        await interaction.response.send_message("**Announcement Sent!**", delete_after=5)
