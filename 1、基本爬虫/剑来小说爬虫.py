import requests
from lxml import etree


def get_html(urls,headers):
    try:
        response = requests.get(urls, headers=headers)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(e,urls)

def get_bookname_url(html):
    html = etree.HTML(html)
    url = html.xpath('//ul[@class="section-list fix"]//a/@href')
    name = html.xpath('//ul[@class="section-list fix"]//a/text()')
    return {k: v for k, v in zip(url[12:], name[12:])}




def get_url_dict():
    url = 'https://www.x81book.com'  # 确保URL是正确的
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    dict_all = {}
    for i in range(2,61):
        if i == 1:
            a = "/book/2987/"
        else:
            a = f"/book/2987/index_{i}.html"
        urls = url + a
        html = get_html(urls, headers)
        url_dict = get_bookname_url(html)
        dict_all.update(url_dict)
    return dict_all

def get_html(urls,headers):
    try:
        response = requests.get(urls, headers=headers)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(e,urls)

def write_world(html):
    html = etree.HTML(html)
    name = html.xpath('//h1/text()')
    chapter = html.xpath('//p/text()')
    if name:
        book_name = name[0].replace(' ', '')
        book_chapter = '\n  '.join(chapter[2:])
    return {
        "book_name": book_name,
        "book_chapter": book_chapter
    }




if __name__ == '__main__':
    url = 'https://www.x81book.com'  # 确保URL是正确的
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    j = 0
    for i,v in get_url_dict().items():
        urls = url + i
        html = get_html(urls,headers)
        w = write_world(html)
        print(w)
        with open(f'I:\python爬虫\\1、基本爬虫\\剑来小说\\{str(j)}{v}.md','w', encoding='utf-8') as file:
            file.write(f'# {w.get("book_name")}\n, {w.get("book_chapter")}')
        j += 1