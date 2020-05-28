import requests
import re
from pyquery import PyQuery as pq


def get_page(urls):
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


def get_page_link(g_page):
    doc = pq(g_page)
    dd = doc('.box_con #list dl dd a')
    result = re.findall('<a href="(.*?)">', str(dd))
    return result


def get_link(urls, links):
    page_link = []
    for link in range(len(links)):
        fiction_link = urls + links[link]
        page_link.append(fiction_link)
    return page_link


def downing(page_links):
    for page_link in range(len(page_links)):
        headers = {
            'host': 'www.jpxs.org',
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser;'
                          ' .NET CLR 1.1.4322; .NET CLR 2.0.50727)'
        }
        r = requests.get(page_links[page_link], headers=headers)
        r.encoding = 'gbk'
        doc = pq(r.text)
        dd = doc('#wrapper .content_read .box_con #content', doc)
        with open('小说.txt', 'a+', encoding='utf-8') as file:
            file.write(dd.text() + '\n')
            file.write('--------------' + '\n')
        print(dd.text())


if __name__ == '__main__':
    urls = 'https://www.jpxs.org'
    g_page = get_page(urls)
    links = get_page_link(g_page)
    page_links = get_link(urls, links)
    page_links.pop()
    downing(page_links)
