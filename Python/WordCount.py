import pandas as pd
from collections import Counter
from fuzzywuzzy import fuzz
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------------------------

# 读取关键词以及权值信息
stomach = pd.read_csv('StomachKeyWords.csv', index_col=False)
flu_like = pd.read_csv('FluLikeKeyWords.csv', index_col=False)

# ----------------------------------------------------------------------------------------------------------------------

# 得到每一天的所有信息
for row in range(21):
    if row == 20:
        row = 29

    print(row+1)

    # 读入文件
    data = pd.read_csv('day_data/'+str(row+1)+'/'+str(row+1)+'.csv', index_col=False)

    # ------------------------------------------------------------------------------------------------------------------
    print('a')

    # 获取当天的所有text
    result = ""

    for i in data.itertuples():
        # 获取字符串
        sentence = getattr(i, 'Text')
        result = result + str(sentence) + '\n'  # 换行

    # 将字符串写入txt文件
    txt = open('day_data/'+str(row+1)+'/'+str(row+1)+'.txt', "w", encoding='utf-8').write(result)

    # ------------------------------------------------------------------------------------------------------------------
    print('b')

    # 对每一天的高频词进行统计
    # 打开txt文件
    txt = open(u'day_data/'+str(row+1)+'/'+str(row+1)+'.txt', "r").read()

    # 绘制词云
    keywords = WordCloud(background_color="white", width=1000, height=1000, margin=2).generate(txt)

    plt.imshow(keywords)
    plt.axis("off")
    plt.show()

    keywords.to_file('day_data/'+str(row+1)+'/'+str(row+1)+'_WordCloud.png')

    # 提取关键词
    freq = Counter(txt.split()).most_common(100000)
    Words = pd.DataFrame()
    word = []
    num = []

    for i in range(len(freq)):
        word.append(freq[i][0])
        num.append(freq[i][1])

    Words['Word'] = word
    Words['Times'] = num

    Words.to_csv('day_data/'+str(row+1)+'/'+str(row+1)+'_Words.csv', index=None)

    # ------------------------------------------------------------------------------------------------------------------
    print('c')

    # 统计每个关键词的出现的数量
    data1 = pd.read_csv('day_data/'+str(row+1)+'/'+str(row+1)+'_Words.csv', index_col=False, encoding='unicode_escape')

    stomach_keywords_data = pd.DataFrame()
    flu_like_keywords_data = pd.DataFrame()

    stomach_keywords = []
    stomach_keynum = []
    flu_like_keywords = []
    flu_like_keynum = []

    # 模糊匹配所有胃疼关键词
    for i in stomach.itertuples():
        sum_num = 0

        # 遍历所有关键词，筛选出符合符合权值条件的关键词
        for j in data1.itertuples():
            word = getattr(j, 'Word')
            num = getattr(j, 'Times')
            rate = fuzz.ratio(str(word), str(getattr(i, 'Words')))

            # 当匹配度达到权值时，统计符合条件的关键词数量
            if rate > int(getattr(i, 'Rate')):
                sum_num += num

        # 存储关键词
        stomach_keywords.append(getattr(i, 'Words'))
        stomach_keynum.append(sum_num)

    stomach_keywords_data['Words'] = stomach_keywords
    stomach_keywords_data['Num'] = stomach_keynum
    stomach_keywords_data.to_csv('day_data/'+str(row+1)+'/'+str(row+1)+'_StomachacheKeyWords.csv', index=None)

    # 模糊匹配所有流感关键词
    for i in flu_like.itertuples():
        sum_num = 0

        # 遍历所有关键词，筛选出符合符合权值条件的关键词
        for j in data1.itertuples():
            word = getattr(j, 'Word')
            num = getattr(j, 'Times')
            rate = fuzz.ratio(str(word), str(getattr(i, 'Words')))

            # 当匹配度达到权值时，统计符合条件的关键词数量
            if rate > int(getattr(i, 'Rate')):
                sum_num += num

        # 存储关键词
        flu_like_keywords.append(getattr(i, 'Words'))
        flu_like_keynum.append(sum_num)

    flu_like_keywords_data['Words'] = flu_like_keywords
    flu_like_keywords_data['Num'] = flu_like_keynum
    flu_like_keywords_data.to_csv('day_data/'+str(row+1)+'/'+str(row+1)+'_FluKeyWords.csv', index=None)

    # ------------------------------------------------------------------------------------------------------------------
    print('d')

    # 获取患者信息
    # 读取关键词以及权值信息
    stomachache_keywords = list(stomach['Words'])
    flu_keywords = list(flu_like['Words'])

    pattern1 = re.compile('|'.join(stomachache_keywords))
    pattern2 = re.compile('|'.join(flu_keywords))

    stomachache_patients = pd.DataFrame(columns=data.columns)
    flu_patients = pd.DataFrame(columns=data.columns)

    stomachache_id = []
    flu_id = []

    for i in data.itertuples():
        text = getattr(i, 'Text')
        id = getattr(i, 'ID')
        # 构建正则表达式，判断患者属于流感患者还是胃病患者
        patient1 = pattern1.findall(str(text))
        patient2 = pattern2.findall(str(text))

        # 如果已经被判断为患者，则跳过
        if id in stomachache_id or id in flu_id:
            continue

        # 如果为胃病患者
        if patient1:
            info = [getattr(i, 'ID'), getattr(i, 'Year'), getattr(i, 'Month'), getattr(i, 'Day'),
                    getattr(i, 'Hour'), getattr(i, 'Minute'), getattr(i, 'Latitude'), getattr(i, 'Longitude'),
                    getattr(i, 'Text')]
            stomachache_patients.loc[len(stomachache_id)] = info
            stomachache_id.append(getattr(i, 'ID'))

        # 如果为流感患者
        if patient2:
            info = [getattr(i, 'ID'), getattr(i, 'Year'), getattr(i, 'Month'), getattr(i, 'Day'),
                    getattr(i, 'Hour'), getattr(i, 'Minute'), getattr(i, 'Latitude'), getattr(i, 'Longitude'),
                    getattr(i, 'Text')]
            flu_patients.loc[len(flu_id)] = info
            flu_id.append(getattr(i, 'ID'))

    stomachache_patients.to_csv('day_data/'+str(row+1)+'/'+str(row+1)+'_StomachachePatients.csv', index=None, encoding='utf-8')
    flu_patients.to_csv('day_data/'+str(row+1)+'/'+str(row+1)+'_FluPatients.csv', index=None, encoding='utf-8')