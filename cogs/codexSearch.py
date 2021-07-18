from discord.ext import commands
from AionCodexScraper.scraper import Scraper
from utils.helper import embed_message


class Codex(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.scraper = Scraper()

    # TODO fix scraper to work together with the bot
    @commands.command()
    async def item(self, ctx, *arg):
        if len(arg) == 0:
            await ctx.send(embed=embed_message("Insufficient arguments"))
            return
        query = " ".join(arg[0:])
        result = await self.scraper.getFirstItem(query=query)
        await ctx.send(result)
        print(query)
        print(type(query))

    @commands.Cog.listener()
    async def on_ready(self):
        print("Codex cog initialized")