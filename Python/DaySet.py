import pandas as pd

data = pd.read_csv('Microblogs_new.csv')

# 记录已统计的日期
num = 0
day_list = []

for row in data.itertuples():
    day_num = getattr(row, 'Day')
    day_data = pd.DataFrame()

    # 记录日期
    if day_num in day_list:
        continue
    else:
        day_list.append(day_num)
        # 获取所有符合条件的数据
        day_data = data[data.iloc[:, 3].isin([day_num])]
        # 写入文件
        day_data.to_csv('day_data//'+str(day_num)+'//'+str(day_num)+'.csv', index=None, encoding='utf-8')
        num += 1
        print(str(day_num)+'完成,当前进度为'+str(num))
        if num == 21:
            break