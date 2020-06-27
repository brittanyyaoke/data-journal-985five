'''
这个模块用来生成词云图
'''

import jieba
import imageio
import wordcloud

#===========分词===========#

#打开文件
fin = open('titledata.csv',encoding="utf-8")
#读取文件
tcontent = fin.read()
#分词（准确模式）
wordlist = jieba.lcut(tcontent)
#分好的词变成字符串
string= " ".join(wordlist)
STOPWORDS = ['大家','一个','有没有','什么','是不是','感觉','这个','真的','自己','我们','你们','觉得','本组','关于','新人','报道','就是','可以','怎么','还是','不是','小组','其实','一下','没有','不要','看到','现在','那么','很多','时候','如果','一直','一点','一些','各位']

#===========载入背景图片===========#
image = imageio.imread("背景图2.jpeg")

#===========生成词云图===========#

wc = wordcloud.WordCloud(width=1059,height=585,background_color='white',stopwords = STOPWORDS,font_path='simsun.ttc',mask=image,scale=15)

wc.generate(string)
wc.to_file('/Users/brittanyyaoke/PycharmProjects/dbcrawler/标题词云图12.png')
