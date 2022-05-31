import pandas as pd

data = pd.read_csv('Microblogs.csv', encoding='unicode_escape')
data1 = data.copy()

# 对时间进行切片
dates = data1.iloc[:, 1]
# 将时间和日期分割
date = dates.str.split(' ', expand=True)
# day表示日期
days = date[0]
print(days)
# 将具体日期进行分割
days = days.str.split('/', expand=True)
# 年
year = days[2]
# 月
month = days[0]
# 日
day = days[1]

# times表示具体时间
times = date[1]
# 将具体时间也进行分割
time = times.str.split(':', expand=True)
hour = time[0]
minute = time[1]
print(hour)
print(minute)

# 分离经纬度
Location = data1.iloc[:, 2]
loc = Location.str.split(' ', expand=True)
latitude = loc[0]
longitude = loc[1]

data_new = pd.DataFrame()
data_new['ID'] = data1.iloc[:, 0]
data_new['Year'] = year
data_new['Month'] = month
data_new['Day'] = day
data_new['Hour'] = hour
data_new['Minute'] = minute
data_new['Latitude'] = latitude
data_new['Longitude'] = longitude
data_new['Text'] = data1.iloc[:, 3]
data_new.to_csv('Microblogs_new.csv', index=None, encoding='utf-8')

print(data_new)