import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
#rcParams设定好画布的大小
rcParams['figure.figsize'] = 25, 12

#读取数据
data = pd.read_csv("data.csv")
#打印开头几个对象
print(data.head())
#显示数据类型
print('\n Data types:')
print(data.dtypes)

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d')
#---其中parse_dates 表明选择数据中的哪个column作为date-time信息，
#---index_col 告诉pandas以哪个column作为 index
#--- date_parser 使用一个function(本文用lambda表达式代替)，使一个string转换为一个datetime变量
data = pd.read_csv("data.csv", parse_dates=['datatime'], index_col='datatime',date_parser=dateparse)
print(data.head())
print(data.index)

ts = data['value']
moving_avg = ts.rolling(365).mean()
plt.plot(ts, color = 'blue')
plt.plot(moving_avg, color = 'red')

ts_moving_avd_diff = ts - moving_avg
plt.plot(ts_moving_avd_diff, color = 'green')
plt.show()