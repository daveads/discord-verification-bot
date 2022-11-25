from discord.ext import commands
import discord

from src.core.startverify  import StartVerify
from src.core.verifybtn    import VerifyBtn
from src.core.userverify   import UserVerify

class VerificationBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(StartVerify(self))
        self.add_view(VerifyBtn(self))
        self.add_view(UserVerify(self))


    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        c = self.get_guild(1024269429229490186)
        print("guild**********", c)