'''
此模块解析数据并制成表格保存：
   1）将源代码转换成bs格式并提取标题、回应数；
   2）信息存入表格
'''

from bs4 import BeautifulSoup

#==========把网页源代码变成bs格式============#
with open('db网页源代码.text','r',encoding='utf-8') as f:
  yuandaima = f.read()
bs = BeautifulSoup(yuandaima,"html.parser")

#print(bs.prettify()) #变成更好看的方式打印出来看


#===========提取帖子标题并用列表储存============#

trs = bs.find_all('tr')[1:]

titlelist = []
hreflist = []
for tr in trs:
  tds = tr.find_all('td')
  #print(tds)
  #print("="*30)
  for td in tds :
    alist= td.find_all('a')
    for a in alist:
      title = a.get('title')
      if type(title) == str:
        titlelist.append(title)
      href = a.get('href')
      if type(href) == str and 'topic' in href:
        hreflist.append(href)

#print(titlelist)
#print(hreflist)


#===========提取作者昵称并存入列表============#

authorlist = []
for tr in trs:
  td2s = tr.find_all('td',limit=3)[1]
  #print(td2s)
  #print("="*30)
  for td2 in td2s:
    author = td2.string
    if author != "作者":
      authorlist.append(author)

#print(authorlist)

#===========提取帖子回应数并存入列表============#

replycountlist = []
for tr in trs:
  td3s = tr.find_all('td',limit=3)[2]
  #print(td3s)
  #print("="*30)
  for td3 in td3s:
    replycount = td3.string
    # print(replycount)
    if replycount != "回应":
      replycountlist.append(replycount)
#print(replycountlist)



'''
#=======检验是否爬取完整==========#
#计算三个列表中有多少元素，验证是否提取了66页的所有帖子#
#print(len(replycountlist))
#print(len(titlelist))
#print(len(authorlist))
#运行结果都是1650=66*25 每个帖子都抓取成功，总共1650个小组讨论帖子#
'''

#===========制作并保存表格============#
import pandas as pd
#==创建一个自然数列表作为序号列==#
num=list(range(1,1651))
#====生成表格====#
basicinfodata = pd.DataFrame({'序号':num, '作者昵称':authorlist,'讨论标题':titlelist, '回应数':replycountlist,'帖子网址':hreflist})
#生成根据回应数排序好的表格#
infodata_sorted = basicinfodata.sort_values(by='回应数',ascending=False)
titledata = pd.DataFrame(titlelist) [单独生成标题的表格]
#print(basicinfodata)
#====储存表格====#
basicinfodata.to_csv('/Users/brittanyyaoke/PycharmProjects/dbcrawler/basicinfodata.csv',index=False)
#为后续爬取前25个热门帖子做准备，储存根据回应数量排序好的表格#
infodata_sorted.to_csv('/Users/brittanyyaoke/PycharmProjects/dbcrawler/sorteddata.csv',index=False)
#【单独保存的只有标题的表格。为词云图做准备】#
titledata.to_csv('/Users/brittanyyaoke/PycharmProjects/dbcrawler/titledata.csv',index=False)


#print(basicinfodata.sort_values(by='回应数',ascending=False))