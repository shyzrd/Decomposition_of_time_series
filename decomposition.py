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
data = pd.read_csv("data.csv", parse_dates=['datetime'], index_col='datetime',date_parser=dateparse)
print(data.head())
print(data.index)

from statsmodels.tsa.seasonal import seasonal_decompose

def decompose(timeseries):
    
    # 返回包含三个部分 trend（趋势部分） ， seasonal（季节性部分） 和residual (残留部分)
    decomposition = seasonal_decompose(timeseries)
    
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    
    plt.subplot(411)
    plt.plot(timeseries, label='Original')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal,label='Seasonality')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residuals')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
    
    return trend , seasonal, residual

ts = data['value']
trend , seasonal, residual = decompose(ts)

residual.to_csv("stationary_data.csv",index=False,sep=',')
