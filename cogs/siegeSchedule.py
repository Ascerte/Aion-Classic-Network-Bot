from bot.config import TARGET_CHANNEL
from discord.ext import commands
import aiocron
import pytz
import datetime


class Schedule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        timezone = pytz.timezone("Europe/London")
        startTime = datetime.datetime.now()
        self.local_date = timezone.localize(startTime)

        @aiocron.crontab('0 1 * * 2', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            print('yesssss')
            await channel.send("Siel West Siege is starting in ONE hour")

        @aiocron.crontab('30 1 * * 2', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            print('yesssss')
            await channel.send("Siel West Siege is starting in 30 minutes")

        @aiocron.crontab('45 1 * * 2', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            print('yesssss')
            await channel.send("Siel West Siege is starting in 15 minutes")

        @aiocron.crontab('0 2 * * 2', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            print('yesssss')
            await channel.send("Siel West Siege has started")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Siege Scheduler cog initialized")
