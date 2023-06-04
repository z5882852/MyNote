import requests
import re

# 请求页面的函数
def get_page(url):
    # 定义请求头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'}
    try:
        response = requests.get(url=url, headers=headers)  # 发送网络请求
        if response.status_code == 200:  # 判断请求是否成功
            return response.text  # 以文本形式返回整个HTML页面
    except:
        print('请求页面错误！！！')

# 定义解析贴吧网页的爬虫函数，用来获取"police吧"帖子标题、作者、链接和创建时间
def get_posts_info(html):
    posts_title = re.findall(r'class="j_th_tit ">(.+?)</a>', html)   # 帖子标题
    posts_author = re.findall(r'title="主题作者:(.+?)"', html)  # 帖子作者
    posts_href = re.findall(r'href="/p/(.+?)"', html)  # 帖子链接
    post_createtime = re.findall(r'title="创建时间">(.+?)<', html)  # 帖子创建时间
    #print('帖子标题：', posts_title)
    #print('帖子作者：', posts_author)
    #print('帖子链接：', posts_href)
    #print('帖子创建时间：', post_createtime)
    return list(zip(posts_title, posts_author, posts_href, post_createtime))

def save_as_txt(text):   
    with open("posts.txt","a",encoding='utf-8') as f:
        f.write(text + '\n')

# 程序入口
if __name__ == '__main__':
    base_url = 'https://tieba.baidu.com/f?kw=police&ie=utf-8&pn={page}'  # "police吧"基础URL地址
    i = 0
    for i in range(0, 201, 50):  # 每页间隔50，实现循环，共5页
        page_url = base_url.format(page = i)  # 通过format替换切换页码的URL地址
        html = get_page(page_url)  # 调用请求页面的函数，获取整个HTML页面
        posts_data = get_posts_info(html)  # 调用解析贴吧网页的爬虫函数，获取"police"贴吧帖子标题、作者、链接和创建时间
        
        for data in posts_data:
            title = data[0]
            author = data[1]
            href = 'https://tieba.baidu.com/p/' + data[2]
            time = data[3]
            text = title + '\t' + author + '\t' + href + '\t' + time
            save_as_txt(text)
            print("已写入数据：",i)
            i += 1

