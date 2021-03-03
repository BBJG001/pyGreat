import time
import asyncio
import requests
import aiohttp



# 非异步方式
'''
def job(t):
    print('Start job ', t)
    time.sleep(t)               # wait for "t" seconds
    print('Job ', t, ' takes ', t, ' s')

def main():
    [job(t) for t in range(1, 3)]

t1 = time.time()
main()
print("NO async total time : ", time.time() - t1)
# Start job  1
# Job  1  takes  1  s
# Start job  2
# Job  2  takes  2  s
# NO async total time :  3.001530647277832
'''

# async异步方式
# 可以加速的原因是网页响应的问题，大多数情况下，网页响应无法跟上计算机的处理速度
# 所以可以在等待一个网页时，先进行另一个网页的请求
'''
async def job(t):                   # async 形式的功能
    print('Start job ', t)
    await asyncio.sleep(t)          # 等待 "t" 秒, 期间切换其他任务
    print('Job ', t, ' takes ', t, ' s')

async def main(loop):                       # async 形式的功能
    tasks = [
        loop.create_task(job(t)) for t in range(1, 3)
    ]                                       # 创建任务, 但是不执行
    await asyncio.wait(tasks)               # 执行并等待所有任务完成

t1 = time.time()
loop = asyncio.get_event_loop()             # 建立 loop
loop.run_until_complete(main(loop))         # 执行 loop
loop.close()                                # 关闭 loop
print("Async total time : ", time.time() - t1)
# Start job  1
# Start job  2
# Job  1  takes  1  s
# Job  2  takes  2  s
# Async total time :  2.0259742736816406
'''


# 单纯用requests访问
'''
URL = 'https://blog.csdn.net/BBJG_001'
def normal():
    for i in range(2):
        r = requests.get(URL)
        url = r.url
        # print(url)

t1 = time.time()
normal()
print("Normal total time:", time.time()-t1)
# Normal total time: 0.7451720237731934
'''


# 异步的requests——aiohttp
URL = 'https://blog.csdn.net/BBJG_001'
async def job(session, url):
    response = await session.get(url)       # 等待并切换
    return str(response.url)

async def main(loop):
    async with aiohttp.ClientSession() as session:      # 官网推荐建立 Session 的形式
        tasks = [loop.create_task(job(session, URL)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]    # 获取所有结果
        # print(all_results)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print("Async total time:", time.time() - t1)
# Async total time: 0.44501423835754395

