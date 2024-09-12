from multiprocessing import Pool,Manager
from time import sleep

def spider(url_queue):
    while not url_queue.empty():
        try:
            url = url_queue.get(timeout = 1)
            print(url)
            sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    url_queue = Manager().Queue()
    for i in range(1,11):
        url = f'https://www.hupu.com/home/v1/news?pageNo={i}&pageSize=50'
        url_queue.put(url)
    pool = Pool(3)
    pool.apply_async(func=spider,args=(url_queue,))
    pool.apply_async(func=spider,args=(url_queue,))
    pool.apply_async(func=spider,args=(url_queue,))
    pool.close()
    pool.join()