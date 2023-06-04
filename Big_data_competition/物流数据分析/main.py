import pandas as pd

file = '物流数据.csv'
df = pd.read_csv(file, header=0, sep=',', engine='python', encoding='utf-8', keep_default_na=False)
print(df.columns)

data1 = df[df['始发站：省'] == '海外']
# data2 = data1[pd.to_datetime(data1['发货时间']) >= pd.to_datetime('2019-12-11')]

data = data1[['运单编号', '货运公司名称', '始发站：省', '收货客户名称', '收货客户手机', '收货客户地址（收件地址）']]
values = ''
for row in data.values:
    if values != '':
        values += '\n'

    value = " ".join(row)
    values += value
print(values)
with open('07.txt', 'w+', encoding='utf-8') as file:
    file.write(values)