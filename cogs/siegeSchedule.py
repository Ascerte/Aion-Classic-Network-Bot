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

        # SIEL WEST MONDAY
        @aiocron.crontab('0 1 * * 2', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Siel West Siege is starting in ONE hour")

        @aiocron.crontab('30 1 * * 2', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            await channel.send("Siel West Siege is starting in 30 minutes")

        @aiocron.crontab('45 1 * * 2', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Siel West Siege is starting in 15 minutes")

        @aiocron.crontab('0 2 * * 2', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            await channel.send("Siel West Siege has started")

        # KROTAN MONDAY
        @aiocron.crontab('0 3 * * 2', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Krotan Siege is starting in ONE hour")

        @aiocron.crontab('30 3 * * 2', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            await channel.send("Krotan Siege is starting in 30 minutes")

        @aiocron.crontab('45 3 * * 2', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Krotan Siege is starting in 15 minutes")

        @aiocron.crontab('0 4 * * 2', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            await channel.send("Krotan Siege has started")

        # SIEL EAST WEDNESDAY
        @aiocron.crontab('0 1 * * 4', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Siel East Siege is starting in ONE hour")

        @aiocron.crontab('30 1 * * 4', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            await channel.send("Siel East Siege is starting in 30 minutes")

        @aiocron.crontab('45 1 * * 4', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Siel East Siege is starting in 15 minutes")

        @aiocron.crontab('0 2 * * 4', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            await channel.send("Siel East Siege has started")

        # KYSIS WEDNESDAY
        @aiocron.crontab('0 3 * * 4', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Kysis Siege is starting in ONE hour")

        @aiocron.crontab('30 3 * * 4', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            await channel.send("Kysis Siege is starting in 30 minutes")

        @aiocron.crontab('45 3 * * 4', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Kysis Siege is starting in 15 minutes")

        @aiocron.crontab('0 4 * * 4', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            await channel.send("Kysis Siege has started")

        # SULFUR FRIDAY
        @aiocron.crontab('0 1 * * 6', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Sulfur Siege is starting in ONE hour")

        @aiocron.crontab('30 1 * * 6', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            await channel.send("Sulfur Siege is starting in 30 minutes")

        @aiocron.crontab('45 1 * * 6', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Sulfur Siege is starting in 15 minutes")

        @aiocron.crontab('0 2 * * 6', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            await channel.send("Sulfur Siege has started")

        # MIREN FRIDAY
        @aiocron.crontab('0 3 * * 6', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Miren Siege is starting in ONE hour")

        @aiocron.crontab('30 3 * * 6', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            await channel.send("Miren Siege is starting in 30 minutes")

        @aiocron.crontab('45 3 * * 6', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Miren Siege is starting in 15 minutes")

        @aiocron.crontab('0 4 * * 6', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            await channel.send("Miren Siege has started")

        # LOWER ALL SATURDAY
        @aiocron.crontab('0 22 * * 6', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Lower-ALL Siege is starting in ONE hour")

        @aiocron.crontab('30 22 * * 6', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            await channel.send("Lower-ALL Siege is starting in 30 minutes")

        @aiocron.crontab('45 22 * * 6', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Lower-ALL Siege is starting in 15 minutes")

        @aiocron.crontab('0 23 * * 6', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            await channel.send("Lower-ALL Siege has started")

        # UPPER OUTER SATURDAY
        @aiocron.crontab('0 0 * * 0', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Upper OUTER Siege is starting in ONE hour")

        @aiocron.crontab('30 0 * * 0', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            await channel.send("Upper OUTER Siege is starting in 30 minutes")

        @aiocron.crontab('45 0 * * 0', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Upper OUTER Siege is starting in 15 minutes")

        @aiocron.crontab('0 1 * * 0', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            await channel.send("Upper OUTER Siege has started")

        # UPPER INNER SUNDAY
        @aiocron.crontab('0 0 * * 1', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Upper INNER Siege is starting in ONE hour")

        @aiocron.crontab('30 0 * * 1', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel()
            await channel.send("Upper INNER Siege is starting in 30 minutes")

        @aiocron.crontab('45 0 * * 1', self.local_date)
        async def mondaySielWest():
            channel = bot.get_channel(TARGET_CHANNEL)
            await channel.send("Upper INNER Siege is starting in 15 minutes")

        @aiocron.crontab('0 1 * * 1', self.local_date)
        async def mondaySielWest():
            channel = self.bot.get_channel(TARGET_CHANNEL)
            await channel.send("Upper INNER Siege has started")


    @commands.Cog.listener()
    async def on_ready(self):
        print("Siege Scheduler cog initialized")
