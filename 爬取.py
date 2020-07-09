#-*- coding:utf-8 -*-
import requests
import re
from pyquery import PyQuery as pq


# 获取网页https://www.jpxs.org/32_32889源代码
def get_page(urls):
    # 定义headers
    headers = {
        'host': 'www.jpxs.org',
        'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser;'
                      ' .NET CLR 1.1.4322; .NET CLR 2.0.50727)'
    }
    url = urls + '/32_32889'
    r = requests.get(url, headers=headers)
    r.encoding = 'gbk'
    if r.status_code == 200:
        return r.text
    return None


# 获得每个章节的链接
def get_page_link(g_page):
    # 创建pyquery对象，解析出各个章节的链接
    doc = pq(g_page)
    dd = doc('.box_con #list dl dd a')
    result = re.findall('<a href="(.*?)">', str(dd))
    return result

# 构建各个章节的链接并保存到列表中
def get_link(urls, links):
    page_link = []
    for link in range(len(links)):
        fiction_link = urls + links[link]
        page_link.append(fiction_link)
    return page_link


# 请求各个章节并下载保存到文件中
def downing(page_links):
    for page_link in range(len(page_links)):
        headers = {
            'host': 'www.jpxs.org',
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser;'
                          ' .NET CLR 1.1.4322; .NET CLR 2.0.50727)'
        }
        r = requests.get(page_links[page_link], headers=headers)
        r.encoding = 'gbk'
        # 构建pyquery对象，并使用css解析内容
        doc = pq(r.text)
        dd = doc('#wrapper .content_read .box_con #content', doc)
        # 保存到text文件中
        with open('小说.txt', 'a+', encoding='utf-8') as file:
            file.write(dd.text() + '\n')
            file.write('--------------' + '\n')
        print(dd.text())


if __name__ == '__main__':
    urls = 'https://www.jpxs.org'
    g_page = get_page(urls)
    links = get_page_link(g_page)
    page_links = get_link(urls, links)
    page_links.pop()      # 清除最后一个junk
    downing(page_links)
