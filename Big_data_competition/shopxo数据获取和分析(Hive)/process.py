from read_data import read_data_split
from collections import Counter

def process():
    file = read_data_split('goods1.txt', '\t')
    title = []
    for data in file:
        title_0 = data[1].split(" ")
        if title_0[0] == '华为HUAWEI':
            title_0.pop(0)
            for t in title_0:
                title.append(t)
        print(len(title))
    i = 1
    counter = Counter(title)
    counter = sorted(counter.items(),key=lambda x:x[1],reverse=True)
    for dat in counter:
        if i > 6:
            break
        print(f"{dat[0]} {dat[1]}")
        i += 1
    
process()