import pandas as pd

data = pd.read_csv('Weather.csv', encoding='unicode_escape')

# 对时间进行切片
dates = data.iloc[:, 0]
# 将具体日期进行分割
days = dates.str.split('/', expand=True)
# 年
year = days[2]
# 月
month = days[0]
# 日
day = days[1]

data_new = pd.DataFrame()
data_new['Year'] = year
data_new['Month'] = month
data_new['Day'] = day
data_new['Weather'] = data.iloc[:, 1]
data_new['Average_Wind_Speed'] = data.iloc[:, 2]
data_new['Wind_Direction'] = data.iloc[:, 3]
data_new.to_csv('Weather_new.csv', index=None, encoding='utf-8')