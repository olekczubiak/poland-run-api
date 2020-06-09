import aiohttp
import asyncio
import time

##work

async def download_file(url):
    print(f'started downloading {url}')
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get(url) as resp:
            content = await resp.read()
            print(f'Finished downloading {url}')
            return content

async def write_file(n, content):
    filename = f'async_{n}.html'
    with open(filename, 'wb') as f:
        print(f'Started writting {filename}')
        f.write(content)
        print(f'Finished writting {filename}')


async def scrape_tasks(n, url):
    content = await download_file(url)
    await write_file(n, content)


async def main():
    tasks = []
    for n, url in enumerate(open('urls.txt').readlines()):
        tasks.append(scrape_tasks(n, url))
    await asyncio.wait(tasks)

if __name__ == "__main__":
    t = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter() - t
    print(f'Total time taken {t2:02f} seconds')