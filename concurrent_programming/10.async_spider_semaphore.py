import asyncio
import aiohttp
import blog_spider
import time

semaphore = asyncio.Semaphore(10)


async def async_spider_craw(url):
    async with semaphore:
        print("craw url: ", url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                result = await response.text()
                await asyncio.sleep(5)
                print(f"craw url: {url}, {len(result)}")


loop = asyncio.get_event_loop()

tasks = [loop.create_task(async_spider_craw(url)) for url in blog_spider.urls]

start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("use time seconds: ", end - start)
