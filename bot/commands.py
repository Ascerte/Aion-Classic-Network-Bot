import discord
from discord.ext import commands
import asyncio, datetime
from discord.utils import get
import aiocron
import pytz
from bot.config import BOT_TOKEN

timezone = pytz.timezone("Europe/London")
startTime = datetime.datetime.now()
local_date = timezone.localize(startTime)
#local_date = timezone.localize(datetime(2017, 3, 26))
print("Today's date:", local_date)


bot = commands.Bot(command_prefix='!')
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Bot initialized successfully")

@bot.command()
async def test(ctx):
    await ctx.send("I'm alive OwO")


@aiocron.crontab('0 1 * * 2', local_date)
async def mondaySielWest():
    channel = bot.get_channel(864207932660908083)
    print('yesssss')
    await channel.send("Siel West in ONE hour")

@aiocron.crontab('25 0 * * 2', local_date)
async def mondaySielWest():
    channel = bot.get_channel(864207932660908083)
    print('yesssss')
    await channel.send("Siel West in ONE hour")

bot.run(BOT_TOKEN)
