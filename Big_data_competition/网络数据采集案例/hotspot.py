import requests
from lxml import etree

# 处理字符串中的空白符，并拼接字符串
def processing(strs):
    s = ''  # 定义保存内容的字符串
    for n in strs:
        n = ''.join(n.split(" "))  # 去除空白符
        s = s + n  # 拼接字符串
    return s  # 返回拼接后的字符串

# 定义解析页面函数，用来获取百度实时热点排行榜信息
def get_hotspot_info(url, headers):
    response = requests.get(url=url, headers=headers)  # 发送网络请求
    html = etree.HTML(response.text)  # 解析HTML字符串
    div_all = html.xpath('//div[@class="category-wrap_iQLoo horizontal_1eKyQ"]')  # 获取实时热点相关所有信息
    for div in div_all:
        rank = div.xpath('.//div[contains(@class, "index_1Ew5p")]')[0].xpath("string(.)") # 获取实时热点排名
        rank = processing(rank)  # 处理实时热点排名
        title = div.xpath('.//div[@class="c-single-text-ellipsis"]')[0].xpath("string(.)")  # 获取实时热点标题
        title = processing(title)  # 处理实时热点标题
        index = div.xpath('.//div[@class="hot-index_1Bl1a"]')[0].xpath("string(.)")  # 获取实时热点热搜指数
        index = processing(index)  # 处理实时热点热搜指数
        record = rank + '\t' + title + '\t' + index  # 拼接百度实时热点排行榜信息
        print(record)  # 输出


# 程序入口
if __name__ == '__main__':
    url = 'https://top.baidu.com/board?tab=realtime'  # 百度实时热点排行榜链接
    h = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
    }
    get_hotspot_info(url, h) # 调用爬虫方法，获取百度实时热点排行榜信息