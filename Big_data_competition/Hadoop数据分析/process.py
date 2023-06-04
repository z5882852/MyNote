def process():
    '''
    将theft.csv时间字段的格式转换为 YYYY-MM-DD HH:MM:SS
    '''
    infos = read_file()
    datas = ''
    for info in infos:
        data = info.split(',')
        data[4] = data[4].replace('元', '')
        data[6] = time_format(data[6])
        data[7] = time_format(data[7])
        data[9] = time_format(data[9])
        data[10] = time_format(data[10])
        datas += ','.join(data)
    with open('theft_1.csv', 'w', encoding='utf-8') as f:
       f.write(datas)

def read_file():
    with open('theft.csv', 'r', encoding='utf-8') as f:
        return f.readlines()

def time_format(str):
    return str.replace('年', '-').replace('月', '-').replace('日', '').replace('时', ':').replace('分', ':').replace('秒', '')

process()