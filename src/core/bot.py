from discord.ext import commands
import discord

from src.core.startverify  import StartVerify
from src.core.verifybtn    import VerifyBtn
from src.core.selfieverify  import SelfieVerify
from src.btns.custom_decline_btn import custom_decline
from src.btns.decline_btn import DeclineBtn

from src.core.config_parser import BotConfigs



bot_configs = BotConfigs()


class VerificationBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(StartVerify(self))
        self.add_view(VerifyBtn(self))
        self.add_view(SelfieVerify(self))
        self.add_view(custom_decline())
        self.add_view(DeclineBtn())



    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        c = self.get_guild(bot_configs.guild_id())
        print("guild**********", c)
        print('------')