from discord.ext import commands
import aiohttp
from bot.config import BOT_TOKEN
from cogs.codexSearch import Codex
from cogs.siegeSchedule import Schedule


class AionBot(commands.Bot):
    def __init__(self, **options):
        super().__init__(**options)
        self.session = aiohttp.ClientSession()

    async def on_ready(self):
        print('Bot initialized successfully')


bot = AionBot(command_prefix="!")
bot.add_cog(Schedule(bot))
bot.add_cog(Codex(bot))
bot.run(BOT_TOKEN)
