#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
该模块针对豆瓣小组中一些热门帖子制作词云
"""

import jieba

import imageio

import wordcloud

import matplotlib.pyplot as plt

import csv

#打开保存的csv文件并进行分词
file1 = open('做题家概念的起源.csv',encoding="utf-8")

content1 = file1.read()

wordlist1=jieba.cut(content1,cut_all=False)

string1= " ".join(wordlist1)

#载入停词表
sw=open('cn_stopwords.txt',encoding = 'utf-8')
stopwordstext=sw.read()
STOPWORDS= stopwordstext.split("\n")   

#生成词云并保存
image1 = imageio.imread('ph1.png')

wc1=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image1,
    collocations=False,
    stopwords=STOPWORDS,
    scale=5)

wc1.generate(string1)

plt.imshow(wc1)
plt.axis('off')
plt.show()

wc1.to_file('词云图小镇做题家.png') 


# In[2]:


file2 = open('非做题家废物.csv',encoding="utf-8")

content2 = file2.read()

wordlist2=jieba.cut(content2,cut_all=False)

string2= " ".join(wordlist2)

image2 = imageio.imread("ph2.png")

wc2=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image2,
    stopwords=STOPWORDS,
    scale=5)

wc2.generate(string2)


plt.imshow(wc2)
plt.axis('off')
plt.show()

wc2.to_file('词云图非做题家.png') 


# In[3]:


file3 = open('城市对应概念.csv',encoding="utf-8")

content3 = file3.read()

wordlist3=jieba.cut(content3,cut_all=False)

string3= " ".join(wordlist3)

image3 = imageio.imread("ph3.png")

wc3=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image3,
    stopwords=STOPWORDS,
    scale=5)

wc3.generate(string3)


plt.imshow(wc3)
plt.axis('off')
plt.show()

wc3.to_file('词云图城市.png') 


# In[4]:


file4 = open('成为废物的原因.csv',encoding="utf-8")

content4 = file4.read()

wordlist4=jieba.cut(content4,cut_all=False)

string4= " ".join(wordlist4)

image4 = imageio.imread("ph4.png")

wc4=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image4,
    stopwords=STOPWORDS,
    scale=5)

wc4.generate(string4)

plt.imshow(wc4)
plt.axis('off')
plt.show()

wc4.to_file('词云图原因.png') 


# In[32]:




file5 = open('人格类型.csv',encoding="utf-8")

content5= file5.read()

content5.lower()

wordlist5=jieba.cut(content5,cut_all=False)

string5= " ".join(wordlist5)


image5 = imageio.imread("ph5.png")

wc5=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image5,
    stopwords=STOPWORDS,
    scale=5)

wc5.generate(string5)

plt.imshow(wc5)
plt.axis('off')
plt.show()

wc5.to_file('词云图人格类型.png')  


# In[8]:


file6= open('令人窒息的父母.csv',encoding="utf-8")

content6 = file6.read()

wordlist6=jieba.cut(content6,cut_all=False)

string6= " ".join(wordlist6)

image6= imageio.imread("ph6.png")

wc6=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image6,
    stopwords=STOPWORDS,
    scale=5)

wc6.generate(string6)

plt.imshow(wc6)
plt.axis('off')
plt.show()

wc6.to_file('词云图父母.png') 


# In[9]:


file7= open('体质问题.csv',encoding="utf-8")

content7 = file7.read()

wordlist7=jieba.cut(content7,cut_all=False)

string7= " ".join(wordlist7)

image7= imageio.imread("ph7.png")

wc7=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image7,
    stopwords=STOPWORDS,
    scale=5)

wc7.generate(string7)


plt.imshow(wc7)
plt.axis('off')
plt.show()

wc7.to_file('词云图精力.png') 


# In[10]:


file8= open('艰难的时代.csv',encoding="utf-8")

content8 = file8.read()

wordlist8=jieba.cut(content8,cut_all=False)

string8= " ".join(wordlist8)

file9= open('享受不到时代红利.csv',encoding="utf-8")

content9 = file9.read()

wordlist9=jieba.cut(content9,cut_all=False)

string9= " ".join(wordlist9)

image9= imageio.imread("ph9.jpg")

wc9=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image9,
    stopwords=STOPWORDS,
    scale=5)

wc9.generate(string8+string9)


plt.imshow(wc9)
plt.axis('off')
plt.show()

wc9.to_file('词云图时代.png') 


# In[11]:


file10= open('天马行空的理想职业.csv',encoding="utf-8")

content10 = file10.read()

wordlist10=jieba.cut(content10,cut_all=False)

string10= " ".join(wordlist10)

file11= open('真正的理想.csv',encoding="utf-8")

content11 = file11.read()

wordlist11=jieba.cut(content11,cut_all=False)

string11= " ".join(wordlist11)

file12= open('现实点的理想工作.csv',encoding="utf-8")

content12 = file12.read()

wordlist12=jieba.cut(content12,cut_all=False)

string12= " ".join(wordlist12)

image12= imageio.imread("ph12.png")

wc12=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image12,
    stopwords=STOPWORDS,
    scale=5)

wc12.generate(string10+string11+string12)


plt.imshow(wc12)
plt.axis('off')
plt.show()

wc12.to_file('词云图理想.png') 


# In[12]:


file13= open('感情生活顺利吗.csv',encoding="utf-8")

content13 = file13.read()

wordlist13=jieba.cut(content13,cut_all=False)

string13= " ".join(wordlist13)

image13= imageio.imread("ph13.png")

wc13=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image13,
    stopwords=STOPWORDS,
    scale=5)

wc13.generate(string13)

plt.imshow(wc13)
plt.axis('off')
plt.show()

wc13.to_file('词云图感情生活.png') 


# In[13]:


file14= open('被相亲.csv',encoding="utf-8")

content14 = file14.read()

wordlist14=jieba.cut(content14,cut_all=False)

string14= " ".join(wordlist14)

image14= imageio.imread("ph14.png")

wc14=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image14,
    stopwords=STOPWORDS,
    scale=5)

wc14.generate(string14)

plt.imshow(wc14)
plt.axis('off')
plt.show()

wc14.to_file('词云图相亲.png') 


# In[14]:


file15= open('男朋友认为自己five.csv',encoding="utf-8")

content15 = file15.read()

wordlist15=jieba.cut(content15,cut_all=False)

string15= " ".join(wordlist15)

image15= imageio.imread("ph15.png")

wc15=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image15,
    stopwords=STOPWORDS,
    scale=5)

wc15.generate(string15)

plt.imshow(wc15)
plt.axis('off')
plt.show()

wc15.to_file('词云图男朋友.png') 


# In[15]:


file16= open('中青报的报道.csv',encoding="utf-8")

content16 = file16.read()

wordlist16=jieba.cut(content16,cut_all=False)

string16= " ".join(wordlist16)

image16= imageio.imread("ph16.png")

wc16=wordcloud.WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=image16,
    stopwords=STOPWORDS,
    scale=5)

wc16.generate(string16)

plt.imshow(wc16)
plt.axis('off')
plt.show()

wc16.to_file('词云图中青报.png') 






