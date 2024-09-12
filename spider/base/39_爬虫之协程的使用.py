import aiohttp
import asyncio

async def first():
    async with aiohttp.ClientSession() as session:  #  aiohttp.ClientSession() == import requests 模块
        async with session.get('http://httpbin.org/get') as resp:
            rs = await resp.text()
            print(rs)

headers = {'User-Agent':'aaaaaa123'}
async def test_header():
    async with aiohttp.ClientSession(headers= headers) as session:  #  aiohttp.ClientSession() == import requests 模块
        async with session.get('http://httpbin.org/get') as resp:
            rs = await resp.text()
            print(rs)

async def test_params():
    async with aiohttp.ClientSession(headers= headers) as session:  #  aiohttp.ClientSession() == import requests 模块
        async with session.get('http://httpbin.org/get',params={'name':'bjsxt'}) as resp:
            rs = await resp.text()
            print(rs)

async def test_cookie():
    async with aiohttp.ClientSession(headers= headers,cookies={'token':'sxt123id'}) as session:  #  aiohttp.ClientSession() == import requests 模块
        async with session.get('http://httpbin.org/get',params={'name':'bjsxt'}) as resp:
            rs = await resp.text()
            print(rs)

async def test_proxy():
    async with aiohttp.ClientSession(headers= headers,cookies={'token':'sxt123id'}) as session:  #  aiohttp.ClientSession() == import requests 模块
        async with session.get('http://httpbin.org/get',params={'name':'bjsxt'},proxy = 'http://name:pwd@ip:port' ) as resp:
            rs = await resp.text()
            print(rs)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_cookie())