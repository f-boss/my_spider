#-*- coding:utf-8 -*-
import os
import time
import requests
from concurrent import futures

MAX_WORKERS = 50
M3U8_FILE = 'index.m3u8'
BASE_URL = 'https://iqiyi.cdn9-okzy.com/20200704/12013_44dfc9ce/1000k/hls/' 
M3U8_URL = 'https://iqiyi.cdn9-okzy.com/20200704/12013_44dfc9ce/1000k/hls/index.m3u8'
HEADERS = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400',
    'Referer': 'https://www.pianku.tv/py/lJ2ZpBza40Wa_12.html?158778',
}
PATH = 'video/'


# 读取本地的m3u8文件，并创建一个存储文件夹
def read_m3u8():
    with open(PATH+M3U8_FILE, 'r') as file:
        ls = []
        line = " "
        while line:
            line = file.readline()
            if line != '' and line[0] != '#':
                ls.append(line[:-1])
    return ls


# 请求ts链接
def get_ts(url):
    print("正在下载:"+url)
    r = requests.get(BASE_URL+url, headers=HEADERS)
    return r.content


# 单个下载任务
def download_one(url):
    resp = get_ts(url)
    with open(PATH+"ts/"+url, 'wb') as fi:
        fi.write(resp)
    print(url+'下载完成')


# 并发下载任务
def download_many(ul):
    with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
        for url in ul:
            executor.submit(download_one, url)


# 下载m3u8并创建一个文件夹保存
def download_m3u8():

    if os.path.exists(PATH+'ts'):
        pass
    else:
        os.makedirs(PATH+'ts')
    
    r = requests.get(M3U8_URL,headers=HEADERS)
    print("m3u8文件下载完成")
    with open(PATH+M3U8_FILE, 'w') as f:
        f.write(r.text)


def combine_mp4():
    files = os.listdir(PATH+"ts/")
    for file in files:
        if os.path.exists(PATH+"ts/"+file):
            with open(PATH + "ts/" + file, 'rb') as f1:
                with open(PATH + "video.mp4", 'ab') as f2:
                    f2.write(f1.read())
        else:
            print("失败")


# 主函数
def main(download_many):
    download_m3u8()
    urls_list = read_m3u8()
    start = time.time()
    download_many(urls_list)
    end = time.time()
    print("下载完成\n"+'{}个文件共耗时{:.2f}s'.format(len(urls_list), end-start))
    time.sleep(2)
    print('开始合并MP4文件')
    combine_mp4()


if __name__ == '__main__':
    main(download_many)

