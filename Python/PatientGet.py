import pandas as pd
from collections import Counter
from fuzzywuzzy import fuzz
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data_Sto = pd.DataFrame()
data_Flu = pd.DataFrame()

# 读入文件
data1 = pd.read_csv('day_data/' + str(1) + '/' + str(1) + '_StomachacheKeyWords.csv', index_col=False)
data2 = pd.read_csv('day_data/' + str(1) + '/' + str(1) + '_FluKeyWords.csv', index_col=False)
data_Sto['Words'] = data1.iloc[:, 0]
data_Flu['Words'] = data2.iloc[:, 0]

# ----------------------------------------------------------------------------------------------------------------------

# 得到每一天的关键词信息
for row in range(21):
    if row == 20:
        row = 29

    print(row+1)

    # 读入文件
    data1 = pd.read_csv('day_data/'+str(row+1)+'/'+str(row+1)+'_StomachacheKeyWords.csv', index_col=False)
    data2 = pd.read_csv('day_data/'+str(row+1)+'/'+str(row+1)+'_FluKeyWords.csv', index_col=False)

    data_Sto[str(row+1)] = data1.iloc[:, 1]
    data_Flu[str(row+1)] = data2.iloc[:, 1]

print(data_Sto)
print(data_Flu)
data_Sto.to_csv('StoDayCount.csv', index=False)
data_Flu.to_csv('FluDayCount.csv', index=False)