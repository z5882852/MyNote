import pandas as pd

def save(file_path, list):
    values = ''
    for row in list:
        if values != '':
            values += '\n'
        value = " ".join(row)
        values += value
    with open(file_path, 'w+', encoding='utf-8') as file:
        file.write(values)

def save_(file_path, values):
    with open(file_path, 'w+', encoding='utf-8') as file:
        file.write(values)

def read_data(file_path):
    data = pd.read_csv(file_path, header=0, sep=',', engine='python', encoding='utf-8', keep_default_na=False)
    print(data.columns)
    data_1 = data[data['始发站：省'] == '海外']
    data_2 = data_1[[
        '运单编号',
        '货运公司名称',
        '始发站：省',
        '收货客户名称',
        '收货客户手机',
        '收货客户地址（收件地址）'
    ]]

    print(data_2)
    save('07.txt', data_2.values)


read_data('物流数据.csv')