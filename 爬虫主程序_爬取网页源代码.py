
'''
此模块用于爬取豆瓣"985废物引进计划"小组的热门帖子及其基本信息
'''

'''
get_html是用于爬取网页源代码的函数
'''

import requests
import uagent #导入写好的随机生成代理的模块


def get_html(url_visit):

    ua = uagent.get_ua()
    headers = {"User-Agent": ua}

    try:
        resp = requests.get(url_visit, headers = headers)

        if resp.status_code == 200:
            print ("成功爬取源代码")
            print (resp.text)

            with open("/Users/brittanyyaoke/PycharmProjects/dbcrawler/db网页源代码.text","a") as file:
                file.write(resp.text)

    except Exception as e :
        print ("爬取失败:%s" % e)
    return resp.text


if __name__ == '__main__':

    #定义url并调用函数爬取#
    group_url = "https://www.douban.com/group/692739/discussion?start={}&type=essence"  # 将start=后的数字改为{}先空出来以便一会进行循环设置#
    for i in range(66):  # 要爬取的所有帖子一共有66页 因此需要爬取66次
        start = i * 25
        url_visit = group_url.format(start)
        #调用写好的get_html函数爬取#
        get_html(url_visit)


