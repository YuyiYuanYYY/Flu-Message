import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from fuzzywuzzy import fuzz
import re

# """Count words."""
# def count_words(s, n):
#     """Return the n most frequently occuring words in s."""
#     w = {}
#     sp = s.split()
#     # TODO: Count the number of occurences of each word in s
#     for i in sp:
#         if i not in w:
#             w[i] = 1
#         else:
#             w[i] += 1
#     # TODO: Sort the occurences in descending order (alphabetically in case of ties)
#     top = sorted(w.items(), key=lambda item:(-item[1], item[0]))
#     top_n = top[:n]
#     # TODO: Return the top n most frequent words.
#     return top_n

# ----------------------------------------------------------------------------------------------------------------------

# # 读入EXCEL文件
# data = pd.read_csv('Microblogs.csv', encoding='unicode_escape')
#
# result = ""
# i = 1
#
# for row in data.itertuples():
#     # 获取字符串
#     sentence = getattr(row, 'text')
#     result = result + str(sentence) + '\n'  # 换行
#     print(i)
#     i = i + 1
#
# # 将字符串写入txt文件
# txt = open("text.txt", "w", encoding='utf-8').write(result)

# ----------------------------------------------------------------------------------------------------------------------
# stops = ['is', 'I', 'one', 'i', 'this', 'a', 'the', 'on', 'at', 'what', 'have', 'to', 'be',
#          'want', 'think', 'need', 'will', 'go', 'come',  'my', 'of', 'and', 'not', 'there',
#          'Why', 'for', 'it', 'that', 'can', 'so', 'or', 'get', 'in', 'but', 'wa', 'all', 'out',
#          'do', 'with', 'right', 'when', 'back', 'about', 'off', 'over', 'no', 'new', 'God', 'newtwitter',
#          'love', 'now', 'today', 'day', 'going', 'life', 'time', 'man', 'by', 'just', 'hate', 'am',
#          'lol', 'know', 'feel', 'good', 'still', 'thing', 'twitter', 'mind', 'first', "I'm", 'morning'
#          'way', 'tonight', 'gonna', 'then', 'house', 'was', 'its', 'work', 'down', 'from', 'you', 'here',
#          'u', 'where', 'he', 'your', 'world', 'only', 'them', 'as', 'up', 'got', 'im', 'see', 'case', 'best',
#          'we', 'night', 'has', 'after', 'because', 'phone', 'makes me', 'music', 'D', 'hi', 'well', 'really',
#          'home', 'great', 'caught', 'friend', 'sleep', 'their', 'oh', 'car', 'how', 'his', 'if', 'like', 'me',
#          'she', 'are', 'say', 'more', "don't", 'people', 'who', 'again', 'some', 'getting', 'start', 'watching',
#          'movie', 'killing me', 'last', 'been', 'which', 'more', 'much', 'would', 'guy', 'n', 'girl', 'him', 'thank',
#          'lt', 'look', 'name', 'trying', 'everyone', 'they are', 'they', 'her', 'make', 'had', 'better', 'making',
#          'tweet', 'something', 'long', 'dontyoujusthateitwhen', 'OMG', 'week', 'nothing', 'fun', 'too', 'killing',
#          'nothing', 'tomorrow', 'friends', 'doe', 'boondock', 'ready', 'real', 'show']

# f = open(u'text.txt', 'r').read()

# stopwords = set(stops)
#
# keywords = WordCloud(background_color="white", stopwords=stopwords, width=1920, height=1080, margin=2).generate(f)
#
# plt.imshow(keywords)
# plt.axis("off")
# plt.show()
#
# keywords.to_file('plot7.png')

# ----------------------------------------------------------------------------------------------------------------------

# # 提取关键词
# freq1 = Counter(f.split())
# freq2 = Counter(f.split()).most_common(100000)
# words = pd.DataFrame()
# word = []
# num = []
#
# for i in range(100000):
#     word.append(freq2[i][0])
#     num.append(freq2[i][1])
#
# words['Word'] = word
# words['Times'] = num
#
# words.to_csv('Words.csv', index=None)

# ----------------------------------------------------------------------------------------------------------------------

# # 设计关键词对应模糊匹配权值表
# # 胃病关键词
# stomach = ['stomachache', 'nausea', 'diarrhea', 'vomit', 'pains', 'pain', 'painful']
# stomach_num = [68, 73, 71, 75, 91, 90, 77]
# # 流感关键词
# flu_like = ['flu', 'fever', 'pneumonia', 'chill', 'sweat', 'fatigue', 'cough']
# flu_num = [85, 89, 70, 89, 89, 80, 80]
#
# stomach_keywords = pd.DataFrame()
# flu_keywords = pd.DataFrame()
# stomach_keywords['Words'] = stomach
# stomach_keywords['Rate'] = stomach_num
# flu_keywords['Words'] = flu_like
# flu_keywords['Rate'] = flu_num
# stomach_keywords.to_csv('StomachKeyWords.csv', index=None)
# flu_keywords.to_csv('FluLikeKeyWords.csv', index=None)

# ----------------------------------------------------------------------------------------------------------------------

# # 统计每个关键词的出现的数量
# data = pd.read_csv('Words.csv', index_col=False, encoding='unicode_escape')
#
# stomach_keywords_data = pd.DataFrame()
# flu_like_keywords_data = pd.DataFrame()
#
# # 读取关键词以及权值信息
# stomach = pd.read_csv('StomachKeyWords.csv', index_col=False)
# flu_like = pd.read_csv('FluLikeKeyWords.csv', index_col=False)
#
# stomach_keywords = []
# stomach_keynum = []
# flu_like_keywords = []
# flu_like_keynum = []
#
# # 模糊匹配所有胃疼关键词
# for i in stomach.itertuples():
#     sum_num = 0
#
#     # 遍历所有关键词，筛选出符合符合权值条件的关键词
#     for row in data.itertuples():
#         word = getattr(row, 'Word')
#         num = getattr(row, 'Times')
#         rate = fuzz.ratio(str(word), str(getattr(i, 'Words')))
#
#         # 当匹配度达到权值时，统计符合条件的关键词数量
#         if rate > int(getattr(i, 'Rate')):
#             sum_num += num
#
#     # 存储关键词
#     stomach_keywords.append(getattr(i, 'Words'))
#     stomach_keynum.append(sum_num)
#
# stomach_keywords_data['Words'] = stomach_keywords
# stomach_keywords_data['Num'] = stomach_keynum
# stomach_keywords_data.to_csv('StomachKeyWords.csv', index=None)
#
# # 模糊匹配所有流感关键词
# for i in flu_like.itertuples():
#     sum_num = 0
#
#     # 遍历所有关键词，筛选出符合符合权值条件的关键词
#     for row in data.itertuples():
#         word = getattr(row, 'Word')
#         num = getattr(row, 'Times')
#         rate = fuzz.ratio(str(word), str(getattr(i, 'Words')))
#
#         # 当匹配度达到权值时，统计符合条件的关键词数量
#         if rate > int(getattr(i, 'Rate')):
#             sum_num += num
#
#     # 存储关键词
#     flu_like_keywords.append(getattr(i, 'Words'))
#     flu_like_keynum.append(sum_num)
#
# flu_like_keywords_data['Words'] = flu_like_keywords
# flu_like_keywords_data['Num'] = flu_like_keynum
# flu_like_keywords_data.to_csv('FluKeyWords.csv', index=None)

# ----------------------------------------------------------------------------------------------------------------------

# # 获取患者信息
# data = pd.read_csv('Microblogs_new.csv', index_col=False)
#
# # 读取关键词以及权值信息
# stomach = pd.read_csv('StomachKeyWords.csv', index_col=False)
# flu_like = pd.read_csv('FluLikeKeyWords.csv', index_col=False)
#
# stomach_keywords = list(stomach['Words'])
# flu_keywords = list(flu_like['Words'])
#
# pattern1 = re.compile('|'.join(stomach_keywords))
# pattern2 = re.compile('|'.join(flu_keywords))
#
# stomachache_patients = pd.DataFrame(columns=data.columns)
# flu_patients = pd.DataFrame(columns=data.columns)
#
# stomach_id = []
# flu_id = []
#
# i = 0
#
# for row in data.itertuples():
#     i += 1
#     print(i)
#     text = getattr(row, 'Text')
#     id = getattr(row, 'ID')
#     # 构建正则表达式，判断患者属于流感患者还是胃病患者
#     patient1 = pattern1.findall(str(text))
#     patient2 = pattern2.findall(str(text))
#
#     # 如果已经被判断为患者，则跳过
#     if id in stomach_id or id in flu_id:
#         continue
#
#     # 如果为胃病患者
#     if patient1:
#         info = [getattr(row, 'ID'), getattr(row, 'Year'), getattr(row, 'Month'), getattr(row, 'Day'),
#                 getattr(row, 'Hour'), getattr(row, 'Minute'), getattr(row, 'Latitude'), getattr(row, 'Longitude'),
#                 getattr(row, 'Text')]
#         stomachache_patients.loc[len(stomach_id)] = info
#         stomach_id.append(getattr(row, 'ID'))
#
#     # 如果为流感患者
#     if patient2:
#         info = [getattr(row, 'ID'), getattr(row, 'Year'), getattr(row, 'Month'), getattr(row, 'Day'),
#                 getattr(row, 'Hour'), getattr(row, 'Minute'), getattr(row, 'Latitude'), getattr(row, 'Longitude'),
#                 getattr(row, 'Text')]
#         flu_patients.loc[len(flu_id)] = info
#         flu_id.append(getattr(row, 'ID'))
#
# stomachache_patients.to_csv('StomachachePatients.csv', index=None, encoding='utf-8')
# flu_patients.to_csv('FluPatients.csv', index=None, encoding='utf-8')
