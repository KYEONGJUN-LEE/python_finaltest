import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#판다스로 읽어와서 그래프화 시키기
gdp= pd.read_csv('나라별_GDP.csv',index_col=0)
korea = gdp[['korea_gdp']]
japan = gdp[['japan_gdp']]
china = gdp[['china_gdp']]
plt.plot(korea,label = 'korea')
plt.plot(japan,label = 'japan')
plt.plot(china,label = 'china')

plt.xlabel('year')
plt.legend()

#판다스를 넘파이로 형변환시켜서 값구하기
korea_price = np.array(korea)
print('한국GDP평균',np.mean(korea_price))
print('한국GDP최댓값',np.max(korea_price))
print('한국GDP최솟값',np.min(korea_price))
print('한국GDP중앙값',np.median(korea_price))
plt.show()
