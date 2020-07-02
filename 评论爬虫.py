'''
此模块用于爬取选出的豆瓣"985废物引进计划"的帖子下的评论，并分别保存
'''

'''
使用提示：
此代码有四处需要注意：
1）爬取新的帖子时，需保证工作目录下没有"评论页代码.text"文件，否则需要先删除该文件
2）需要将帖子所在页面url粘贴至comment_url变量内
3）需要根据帖子下的评论页数修改爬取的for循环中的range（）
4）需要根据帖子主题修改合适的文件名并保存
'''

import requests
import uagent
import pandas as pd
from lxml import etree
import os
import sys


#==爬虫函数，爬取源代码==#
def get_html(url_visit):

    ua = uagent.get_ua()
    headers = {"User-Agent": ua}

    try:
        resp = requests.get(url_visit, headers=headers)

        if resp.status_code == 200:
            print("成功爬取源代码")
                # print (resp.text)
            with open("/Users/brittanyyaoke/PycharmProjects/dbcrawler/评论页代码.text", "a") as file:  # 使用时需要修改路径
                file.write(resp.text)

    except Exception as e:
        print("爬取失败:%s" % e)
    return resp.text

if __name__ == '__main__':
    comment_url = "https://www.douban.com/group/topic/180487605/"  # 1）需替换为需要爬取的网址 2）将start=后的数字改为{}先空出来以便一会进行循环设置#
    
    #判断当前工作目录下是否已经存在“评论页代码.text”这个文件，有则需要先删除#
    if os.path.exists("评论页代码.text"):
        print("请先删除当前工作目录下的评论页代码文件")
        sys.exit()
    else:
        for i in range(5):  # 要爬取的评论页数 根据评论实际有几页来修改
            start = i * 100
            url_visit = comment_url.format(start)
        # 调用写好的get_html函数爬取#
            get_html(url_visit)

#====解析部分====#

with open('评论页代码.text', 'r', encoding='utf-8') as f:
    html = f.read()
    comments = []
    html = etree.HTML(html)
    lis = html.xpath("// ul[ @class ='topic-reply']/li")
    for li in lis:
        content = li.xpath(".//div[@class ='reply-doc content']/p/text()")[0]
        comments.append(content)
        commentdata = pd.DataFrame({'评论': comments})

#====保存为csv文件====#
#print(commentdata)
commentdata.to_csv("讨论主题.csv")


