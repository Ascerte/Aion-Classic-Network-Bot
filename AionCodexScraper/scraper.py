import asyncio
import aiohttp
from bs4 import BeautifulSoup


class Scraper:
    url = "https://aioncodex.com/query.php"

    async def getSearchResultTable(self, query):
        params = {"a": "search", "l": "usc", "sq": query}
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, params=params) as resp:
                print(resp.status)
                return await resp.json(content_type='text/html')

    async def run(self, query):
        table = await self.getSearchResultTable(query)
        return table

    async def getFirstItem(self, entityType=None, query=""):
        loop = asyncio.get_event_loop()
        table = loop.run_until_complete(self.run(query))
        data = table['aaData'][1][2]
        parsedHTML = BeautifulSoup(data, features="lxml")
        return parsedHTML.text, parsedHTML.a["href"]
