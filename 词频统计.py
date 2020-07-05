#!/usr/bin/env python
# coding: utf-8

# In[6]:


"""
该模块针对小组内“来大家写下让自己废掉的专业 ”和“大家进来说说自己后悔没选的学校or专业”进行词频分析，
统计出现最多的专业名称

"""

import jieba

import imageio

import wordcloud

import matplotlib.pyplot as plt

import csv

from collections import Counter

#载入停词表
sw=open('cn_stopwords.txt',encoding = 'utf-8')
stopwordstext=sw.read()
STOPWORDS= stopwordstext.split("\n")   

file17 = open('让自己废掉的专业.csv',encoding="utf-8")

#使用结巴分词
content17 = file17.read()
wordlist17=jieba.cut(content17,cut_all=False)

#去掉wordlist17中包含在停词表内的词语
majorlist=[]
for x in wordlist17:
    if x not in STOPWORDS:
        majorlist.append(x)

#词频统计
c1=Counter()
for x in majorlist:
    if len(x)>1 and x != '\r\n':
        c1[x] += 1
        
# 输出词频最高的前100个词
print('\n词频统计结果：')
for (k,v) in c1.most_common(100):
    print("%s:%d"%(k,v))


# In[ ]:


file18 = open('后悔没选的专业.csv',encoding="utf-8")

content18 = file18.read()
wordlist18=jieba.cut(content18,cut_all=False)

majorlist_n=[]
for x in wordlist18:
    if x not in STOPWORDS:
        majorlist_n.append(x)
        
c2=Counter()
for x in majorlist_n:
    if len(x)>1 and x != '\r\n':
        c2[x] += 1

print('\n词频统计结果：')
for (k,v) in c2.most_common(100):# 输出词频最高的前两个词
    print("%s:%d"%(k,v))

