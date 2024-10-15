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
    for i in range(1,3):
        if i == 1:
            a = "/book/2987/"
        else:
            a = f"/book/2987/index_{i}.html"
        urls = url + a
        html = get_html(urls, headers)
        url_dict = get_bookname_url(html)
        dict_all.update(url_dict)
