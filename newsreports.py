#!/usr/bin/env python
# coding: utf-8

# In[4]:


from newspaper import Article

url_list=[
    'https://baijiahao.baidu.com/s?id=1668717304303166344&wfr=spider&for=pc',
    'https://baijiahao.baidu.com/s?id=1669279340422319214&wfr=spider&for=pc',
    'https://guancha.gmw.cn/2020-06/18/content_33923516.htm',
    'http://data.163.com/20/0614/20/FF413TIA000181IU.html',
    'http://caozhi.news.163.com/20/0623/10/FFQ4R9TO000181TI.html',
    'https://www.sohu.com/a/403207998_268920',
    'https://www.sohu.com/a/402952855_120179484',
    'https://www.thepaper.cn/newsDetail_forward_7897842',
    'http://www.xinhuanet.com/comments/2020-06/17/c_1126123298.htm'
]

news_title = []  #创建列表
news_text = []
news_publish_date=[]
    
for url in url_list:
    news = Article(url,language='zh')
    
    news.download() #下载并解析新闻
    news.parse()
    
    news_title.append(news.title)  #加入列表
    news_text.append(news.text)   
    news_publish_date.append(news.publish_date) 
    
import pandas as pd
data = pd.DataFrame({'title':news_title,'text':news_text,'date':news_publish_date})
data
data.to_csv("newsreports.csv")

import jieba  #使用结巴分词进行分词
newsreports=' '.join(news_text)
word_list=jieba.cut(newsreports,cut_all=False)

from wordcloud import WordCloud 
import imageio

background=imageio.imread('po.png')
text="/".join(jieba.cut(newsreports))
STOPWORDS=['一个','根据','这个','那个','已经','这些',
           '自己','觉得','对于','一样','一起','一种','以及','什么',
           '就是','可以','怎么','还是','不是','小组','其实','还有','有人',
           '没有','不要','看到','现在','那么','很多','时候',
           '一些']

wc_newsreports=WordCloud(
    font_path='simsun.ttc',
    background_color='white',
    mask=background,
    stopwords=STOPWORDS,
    scale=5).generate(text)

import matplotlib.pyplot as plt

plt.imshow(wc_newsreports)
plt.axis('off')
plt.show()

wc_newsreports.to_file('cloud.png') #储存词云图







    


# In[ ]:





# In[ ]:




