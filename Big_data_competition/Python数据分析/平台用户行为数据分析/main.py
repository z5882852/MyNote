import collections
from read_data import read_csv
import time

def get_data():
    return read_csv('UserBehavior.csv', ',')

def word_counter(list):
    c = collections.Counter(list)
    c = sorted(c.items(),key=lambda x:x[1],reverse=True)
    return c

def t_1():
    '''
    统计每个日期的浏览数(pv)
    '''
    data = get_data()
    temp = []
    for value in data.values:
        if value[4] == 'pv':
            temp.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value[5])).split(' ')[0])
    output = []
    for c_ in word_counter(temp):
        output.append(f"{c_[0]} {c_[1]}")
    return output


if __name__ == '__main__':
    print('\n'.join(t_1()))