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
5）特别注意要修稿with open('评论.text', 'r', encoding='utf-8') as f:这一句中文件的名字，应该与上面的保存的评论.text一致，确保打开的是这个文件
'''

import requests
import uagent #导入写好的随机生成代理的模块
from lxml import etree
import pandas as pd
def get_html(url_visit):

    ua = uagent.get_ua()
    headers = {"User-Agent": ua}

    try:
        resp = requests.get(url_visit, headers = headers)

        if resp.status_code == 200:
            print ("成功爬取源代码")
            print (resp.text)

            with open("/Users/brittanyyaoke/PycharmProjects/dbcrawler/评论.text","a") as file:
                file.write(resp.text)

    except Exception as e :
        print ("爬取失败:%s" % e)
    return resp.text


if __name__ == '__main__':

    #定义url并调用函数爬取#
    group_url = "https://www.douban.com/group/topic/182240673/?start={}"  # 将start=后的数字改为{}先空出来以便一会进行循环设置#
    for i in range(2):
        start = i * 100
        url_visit = group_url.format(start)
        print(url_visit)
        #调用写好的get_html函数爬取#
        get_html(url_visit)

#import pandas as pd

#from lxml import etree

with open('评论.text', 'r', encoding='utf-8') as f:
    html = f.read()
    comments = []
    html = etree.HTML(html)
    lis = html.xpath("// ul[ @class ='topic-reply']/li")
    for li in lis:
        content = li.xpath(".//div[@class ='reply-doc content']/p/text()")[0]
        comments.append(content)
        commentdata = pd.DataFrame({'评论': comments})

#保存为csv文件#
#print(commentdata)
commentdata.to_csv("评论.csv")


