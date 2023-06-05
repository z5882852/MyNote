
## 示例:美化气温折线图

### （1）设置线条和颜色
`color` 参数用于设置线条颜色
`linestyle` 参数用于设置线条的样式
marker参数用于设置标记样式
为“14天气温折线图”设置颜色和线条，并在实际气温位置进行标记

```Python
plt.plot(x, y, color='red', linestyle='-', marker='o')
```

### （2）自定义一个蓝绿色画布
`Matplotlib` 中可以使用 `figure` 函数设置画布大小、分辨率、颜色和边框等。
创建画布大小为6×4(英寸)，背景色为蓝绿色

```Python
plt.figure(figsize=(6, 4), facecolor='aquamarine')
```

### （3）设置坐标轴
x 轴和 y 轴标题主要 `xlabel` 函数和 `ylabel` 函数
下面为气温折线图设置坐标轴标题，其中，设置 x 轴标题为“2022年3月”，y 轴标题为“最高气温”

```Python
plt.xlabel('2022年3月')  # 设置x轴标题
plt.ylabel('最高气温')  # 设置y轴标题
```

### （4）设置坐标范围
坐标轴范围是指 x 轴和 y 轴的取值范围。设置坐标轴范围主要使用 xlim 函数和 ylim 函数
设置 x 轴（日期）范围为0-14，y 轴（气温）范围为4-20

```Python
plt.xlim(0, 14)  # 设置x轴范围
plt.ylim(4, 20)  # 设置y轴范围
```

### （5）设置网格线
在 `Matplotlib` 中可以使用 `grid` 函数生成网格线。
设置网格线灰度值为0.5，线条为双划线，线条宽度为1

```Python
plt.grid(color='gray', linestyle='--', linewidth=1)
```

### （6）为折线图添加文本标签
使用 text 函数给图表中指定的数据点添加文本标签

```Python
for i in range(len(x)):
    plt.text(x[i], y[i], str(y[i]))
```

### （7）为折线图设置标题
为图表设置标题使用 `title` 函数
下面设置图表标题为“北京14天气温折线图”

```Python
plt.title('北京14天气温折线图')
```

### （8）为折线图设置图例
为图表设置图例主要使用 `legend` 函数
为“北京14天气温折线图”添加“气温”图例，显示位置为右下方显示，字体大小设置为10

```Python
plt.legend(['气温'], loc='lower right', fontsize=10)
```

### （9）为折线图添加注释
`annotate` 函数用于在图表上给数据添加文本注释，而且支持带箭头的划线工具，方便我们在合适的位置添加描述信息
在“北京14天气温折线图”中用箭头指示最低气温

```Python
min_temp = min(y)
min_index = y.index(min_temp)
plt.annotate('最低气温', xy=(x[min_index], min_temp), xytext=(x[min_index]-2, min_temp-4),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

```
