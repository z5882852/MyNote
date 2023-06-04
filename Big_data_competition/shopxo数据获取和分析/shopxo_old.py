import requests
from bs4 import BeautifulSoup

def get_goods_info(url, headers):
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        print("获取页面失败")
        return [False]
    if "资源不存在或已被删除" in response.text:
        print("资源不存在或已被删除")
        return [False]
    soup = BeautifulSoup(response.text, "lxml")
    title_ = str(soup.find('h1', class_="detail-title am-margin-bottom-xs").text)
    title = []
    for word in title_.replace('\n', '').split():
        title.append(word)
    title = ' '.join(title)
    price = soup.find('b', class_="goods-price").text
    preview = soup.find_all('span', class_="tm-count")[1].text
    sell_num = soup.find_all('span', class_="tm-count")[0].text
    stock = soup.find('span', class_="stock").text
    news_list = [True, title, price, preview, sell_num, stock]

    return news_list 

def save_as_txt(file_path, text):
    with open(file_path, 'w+', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    url = 'http://101.200.162.163/index.php?s=/index/goods/index/id/{}.html' 
    # 定义请求头信息
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'}
    goods = ''
    for i in range(1,2000):
        good_list = get_goods_info(url.format(i), headers)
        if not good_list[0]:
            continue
        if goods != '':
            goods += '\n'
        good_list.pop(0)
        good_list.insert(0, str(i))
        good = ','.join(good_list)
        print(good)
        with open("goods.txt", 'a+', encoding='utf-8') as f:
            f.write(good + '\n')
        goods += good
    save_as_txt("goods_2.txt", goods)
