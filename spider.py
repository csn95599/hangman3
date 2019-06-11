change
<<<<<<< HEAD
=======


分开交路口的时刻

很快就江湖救急  好久好久和 跨境
hhkjhjbjkjnjkkjkj


          会尽快哈 好看兰蔻l

>>>>>>> parent of 8ed230d... Update spider.py


分开交路口的时刻

很快就江湖救急  好久好久和 跨境
hhkjhjbjkjnjkkjkj




陈思宁就是牛
import json
import timeit
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?">(\d+)</i>.*?title="(.*?)".*?img src="(.*?)".*?"star">(.*?)</p>.*?'
                         +'releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'name':item[1],
            'image':item[2].strip(),
            'actor':item[3].strip()[3:],
            'time':item[4][5:],
            'score':item[5]+item[6]
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()


def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])


