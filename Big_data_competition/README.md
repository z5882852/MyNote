# 2023年'智警杯'比赛


## Python数据分析
### 一些常用的库
* `Numpy`: 提供多维数组对象，各种派生对象（如掩码数组和矩阵），以及用于数组快速操作的各种API，有包括数学、逻辑、形状操作、排序、选择、输入输出、离散傅立叶变换、基本线性代数，基本统计运算和随机模拟等等。
* `Pandas`: pandas是一个强大的分析结构化数据的工具集；它的使用基础是Numpy（提供高性能的矩阵运算）；用于数据挖掘和数据分析，同时也提供数据清洗功能。
* `Matplotlib`: 是Python中最常用的可视化工具之一，可以非常方便地创建海量类型地2D图表和一些基本的3D图表，可根据数据集（DataFrame，Series）自行定义x,y轴，绘制图形（线形图，柱状图，直方图，密度图，散布图等等），能够解决大部分的需要。Matplotlib中最基础的模块是pyplot。
* `Requests`: Requests是用Python语言编写，基于 urllib，采用 Apache2 Licensed 开源协议的 HTTP 库。
* `BeautifulSoup`: BeautifulSoup是python的一个库，最主要的功能就是从网页爬取我们  需要的数据。BeautifulSoup将html解析为对象进行处理，全部页面转换为字典或数组。
* `lxml`: lxml是XML和HTML的解析器，其主要功能是解析和提取XML和HTML中的数据；lxml和正则一样，也是用C语言实现的，是一款高性能的python HTML、XML解析器，也可以利用XPath语法，来定位特定的元素及节点信息。
### Numpy
引用模块
```Python
import numpy as np
```
### Pandas
引用模块
```Python
import pandas as pd
```
### Matplotlib
引用模块
```Python
import matplotlib.pyplot as plt
```
### Requests
引用模块
```Python
import requests
```
示例
```Python
response = requests.get('https://www.xxx.com/')  # 发送请求

print(response.text)  # 获取响应内容
print(response.status_code)  # 获取响应状态码
print(response.headers)  # 获取响应头
```

### BeautifulSoup
引用模块
```Python
from bs4 import BeautifulSoup
```
解析HTML代码
```Python
html = BeautifulSoup(text, 'lxml')
```

### lxml
引用模块
```Python
from lxml import etree
```
解析HTML代码
```Python
html = etree.HTML(text)
```

## Hadoop数据分析

### MySQL
```bash
systemctl start mysqld.service # 启动mysql服务
systemctl stop mysqld.service # 停止mysql服务
systemctl restart mysqld.service # 重启mysql服务
systemctl status mysqld.service # 查看mysql服务状态
```

### Hadoop
```bash
start-all.sh # 启动Hadoop集群
stop-all.sh # 关闭Hadoop集群

# 以下为单模块启动
start-dfs.sh # 启动HDFS模块
stop-dfs.sh # 关闭HDFS模块

start-yarn.sh # 启动yarn集群
stop-yarn.sh # 关闭yarn集群
```
以下命令的区别
```bash
hadoop fs [options]
hadoop dfs [options]
hdfs dfs [options]
```
- `hadoop fs`：通用的文件系统命令，针对任何系统，比如本地文件、HDFS文件、HFTP文件、S3文件系统等。
- `hadoop dfs`：特定针对HDFS的文件系统的相关操作，但是已经不推荐使用。
- `hdfs dfs`：与hadoop dfs类似，同样是针对HDFS文件系统的操作，替代hadoop dfs

### HDFS
```bash
hdfs namenode -format # 格式化HDFS文件系统
```


### Hive
```bash
schematool -dbType mysql -initSchema # 初始化Hive元数据库

hive # 进入Hive

create database <库名> # 插件Hive数据库
```