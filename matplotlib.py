import numpy as np
import matplotlib.pyplot as plt
f= open('나라별_GDP.csv','r')
lines = f.readlines()
year = []
korea_gdp = []
japan_gdp = []
china_gdp =[]

gdp = {}

for line in lines[1:]:
    new_line = line.split(',')
    year.append(float(new_line[0]))
    korea_gdp.append(float(new_line[1]))
    japan_gdp.append(float(new_line[2]))
    china_gdp.append(float(new_line[3]))

gdp['year'] = year
gdp['한국'] = korea_gdp
gdp['일본'] = japan_gdp
gdp['중국'] = china_gdp

year = np.array(gdp['year'])
korea = np.array(gdp['한국'])
japan = np.array(gdp['일본'])
china = np.array(gdp['중국'])

print(korea[korea>15000])
print('한국GDP평균',np.mean(korea_gdp))
print('한국GDP최댓값',np.max(korea_gdp))
print('한국GDP최솟값',np.min(korea_gdp))
print('한국GDP중앙값',np.median(korea_gdp))

plt.plot(year,korea_gdp, label = 'korea')
plt.plot(year,japan_gdp,label = 'japan')
plt.plot(year,china_gdp,label = 'china')
plt.xlabel('year')
plt.legend()
plt.show()