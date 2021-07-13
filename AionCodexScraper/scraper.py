import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup


class Scraper:
    url = "https://aioncodex.com/query.php"

    async def getSearchResultTable(self, query):
        params = {"a": "search", "l": "usc", "sq": query}
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, params=params) as resp:
                print(resp.status)
                # with open("output.json", "w") as f:
                #     json.dump(await resp.json(content_type='text/html'), f, sort_keys=True, indent=4)
                return await resp.json(content_type='text/html')

    async def run(self, query):
        #loop.run_until_complete(self.getSearchResultTable())
        table = await self.getSearchResultTable(query)
        return table

    async def getFirstItem(self, entityType=None, query=""):
        loop = asyncio.get_event_loop()
        #table = json.loads(self.getSearchResultTable())
        #table = json.loads(loop.run_until_complete(self.run()))
        table = loop.run_until_complete(self.run(query))
        data = table['aaData'][1][2]
        #print(data)
        parsedHTML = BeautifulSoup(data, features="lxml")
        # print(parsedHTML.text)
        # print(parsedHTML.a["href"])
        return parsedHTML.text, parsedHTML.a["href"]
        #print(parsedHTML)
