import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"]=["SimHei"]

plt.figure(figsize=(6, 4), facecolor='aquamarine')  # 自定义画布大小和背景色

plt.title('北京14天气温折线图')  # 设置图表标题

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
y = [18, 14, 13, 20, 18, 16, 10, 9, 7, 4, 18, 20, 18, 14]

plt.plot(x, y, color='red', linestyle='-', marker='o')  # 绘制折线图，设置线条颜色、样式和标记样式

plt.xlabel('2022年3月')  # 设置x轴标题
plt.ylabel('最高气温')  # 设置y轴标题

plt.xlim(0, 14)  # 设置x轴范围
plt.ylim(4, 20)  # 设置y轴范围

plt.grid(color='gray', linestyle='--', linewidth=1)  # 设置网格线的样式和颜色

for i in range(len(x)):
    plt.text(x[i], y[i], str(y[i]))  # 在每个数据点添加文本标签

min_temp = min(y)
min_index = y.index(min_temp)
plt.annotate('最低气温', xy=(x[min_index], min_temp), xytext=(x[min_index]-2, min_temp-2),
             arrowprops=dict(facecolor='black', arrowstyle='->'))  # 添加注释

plt.legend(['气温'], loc='lower right', fontsize=10)  # 设置图例

plt.show()  # 显示图表
