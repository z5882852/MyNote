import pandas as pd

def save(file_path, list):
    values = ''
    for row in list:
        if values != '':
            values += '\n'
        value = " ".join(row)
        values += value
    print(values)
    with open(file_path, 'w+', encoding='utf-8') as file:
        file.write(values)

def save_(file_path, values):
    with open(file_path, 'w+', encoding='utf-8') as file:
        file.write(values)

def read_data(file_path):
    data = pd.read_csv(file_path, header=0, sep=',', engine='python', encoding='utf-8', keep_default_na=False)
    print(data.columns)
    data_1 = data

    data_2 = data_1[['货运公司名称']].values

    temp = {}
    for dat in data_2:
        try:
            num = temp[dat[0]]
            temp[dat[0]] = num + 1
        except:
            temp[dat[0]] = 1
    out = []
    for name in temp:
        out.append([name, str(temp[name])])

    save('01.txt', out)


read_data('物流数据.csv')