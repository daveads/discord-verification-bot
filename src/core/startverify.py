import asyncio
import discord

from src.core.verifybtn import VerifyBtn


class StartVerify(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        
        
    @discord.ui.button(label='Start Verification', style=discord.ButtonStyle.grey, custom_id='srtv_prs')
    async def srtv(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Click button to Verify", view=VerifyBtn(self.bot), ephemeral=True)
        await asyncio.sleep(120)
        await interaction.delete_original_response()
        
    
"""
Gender
Age
"""
