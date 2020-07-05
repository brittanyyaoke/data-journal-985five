import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#import selenium.webdriver.support.ui as ui

url = "https://www.douban.com/group/topic/181133270/" #评论界面
brower = webdriver.Chrome()

brower.get(url)  #启动chrome浏览器并跳转到网页


brower.find_element_by_class_name("nav-login").click() #找到登录按钮 进行自动登录
time.sleep(1) #延时1秒
brower.find_element_by_class_name("account-tab-account").click() #默认是手机号登录，切换成账号密码登录
time.sleep(1)

user_name = '570950152@qq.com'
password =  'doubanAKE'
brower.find_element_by_id("username").clear() #输入前清空下 用户名
brower.find_element_by_id("username").send_keys(user_name) #输入用户名
brower.find_element_by_id("password").clear()
brower.find_element_by_id("password").send_keys(password)

brower.find_element_by_css_selector("#account > div.login-wrap > div.login-right > div > div.account-tabcon-start > div.account-form > "
                                    "div.account-form-field-submit > a").click()
#wait = brower.WebDriverWait(driver_item,10)

#后面开始 读取评论信息

n = 1  # 页数
count = 0  # 评论数目
i = 4 #设置要爬取的页面总数
#short=[]

while True:
    try:

        results = WebDriverWait(brower, 20, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "reply-doc content")))

        #brower.implicitly_wait(10)
        #wait = ui.WebDriverWait(brower, 10)
        #results = wait.until(lambda brower: brower.find_element_by_xpath("/html[@class='ua-mac ua-webkit']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-16-8 clearfix']/div[@class='article']/ul[@id='comments']/li[@id='2513591600']/div[@class='reply-doc content']/p[@class='reply-content']"))
        #results = brower.find_element_by_xpath("//div[@class='reply-doc content']/p[@class=' reply-content']")
        #print(results)

        for result in results:
            comment = result.find_element_by_tag_name('p').text  # 评论内容
            print(comment)
        if i < 1:
            break
    except Exception as e:
        print(e)

        # 定义url并调用函数爬取#
        comment_url = "https://www.douban.com/group/topic/179453547/?start={}&type=essence"  # 将start=后的数字改为{}先空出来以便一会进行循环设置#
        for i in range(4):
            start = i * 100
            href = comment_url.format(start)
            # 调用写好的get_html函数爬取#

            html = getOnepageComment(href)