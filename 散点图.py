# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 21:04:36 2020

@author: yang
"""
"""
该模块用以生成每个专业在“废掉的专业”和“后悔没选的专业”中出现次数的对比散点图
"""

import numpy as np
import matplotlib.pyplot as plt

#使图片中可以正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

#寻找在两个词频中都出现的专业，以x轴作为在“废掉的专业”帖中出现的词频，y轴作为“后悔没选的专业”中出现的词频绘制散点图
x=[66,60,52,50,48,33,22,41,12,25,28,43,41,34]
y=[15,38,17,9,13,7,17,34,7,9,9,8,7,23]
txt = ['金融','建筑','计算机','会计','数学','文学','法学',
       '师范','心理','历史','物理','经济','医学','设计']
n=np.arange(14)

#写标签
plt.xlabel("后悔选了") 
plt.ylabel("后悔没选") 

#设置随机颜色与大小并生成散点图
c = np.random.rand(14)
s = (30*np.random.rand(14))**2
plt.scatter(x,y,s=s,c=c,marker=(8,1),alpha=0.2)
for i in range(len(x)):
    plt.annotate(txt[i], xy = (x[i], y[i]), xytext = (x[i]+0.1, y[i]+0.1)) 
   
plt.show()
plt.savefig('散点图.png',dpi=300)

