'''
import pprint
with open('PaceData.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.split(',')
        flights[k] = v

if __name__ == '__main__':
    pprint(flights)
'''

# 首字母大写
s = 'I DID NOT MEAN TO SHOUT'

from datetime import datetime


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


# 生成器函数
import requests
import pprint

def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


if __name__ == '__main__':
    # print(s)
    # print(s.title())
    # print(convert2ampm('09:30'))

    # 使用生成器函数
    urls = ('https://www.baidu.com/', 'http://talkpython.fm', 'http://python.org')

    urls_res = {url:size for size,_,url in gen_from_urls(urls)}
    pprint(urls_res)