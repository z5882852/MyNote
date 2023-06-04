import requests
from bs4 import BeautifulSoup

# 定义解析页面函数，用来获取网易新闻热点排行Top10信息
def get_news_info(url, headers):
    response = requests.get(url=url, headers=headers)  # 发送网络请求
    soup = BeautifulSoup(response.text, "lxml")  # 创建一个BeautifulSoup对象，获取页面正文
    all_news = soup.find('div', class_="mod_hot_rank").find('ul').find_all('li')  # 获取网易新闻热点排行Top10内容
    news_list = []  # 创建空列表
    for news in all_news:
        news_rank = news.em.string  # 获取新闻排名
        news_title = news.a.string  # 获取新闻标题
        posts_num = news.span.string  # 获取新闻跟帖数
        news_url = news.a.get('href')  # 获取新闻链接
        news_list.append([news_rank, news_title, posts_num, news_url])  # 把每条新闻的排名、标题、跟帖数和链接添加到一个列表中，再追加到一个大列表中
    return news_list  # 返回列表

# 程序入口
if __name__ == '__main__':
    url = 'https://news.163.com/'  # 网易新闻首页链接
    # 定义请求头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'}
    news_list = get_news_info(url, headers)  # 调用爬虫方法，获取网易新闻热点排行Top10
    print(news_list)  # 输出网易新闻热点排行Top10信息