from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
#Browser = webdriver.PhantomJS(executable_path="C:\\Users\skydownacai\Desktop\phantomjs.exe")
Browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
Browser.get("http://weixin.sogou.com")
time.sleep(2)
delun = Browser.find_element_by_xpath("//a[@id='loginBtn']").click()
time.sleep(8)
style1 ="margin: 0.8em 0; padding: 0.6em; border: 1px solid #c0c8d1; border-radius: 0.3em; box-shadow: #aaa 0 0 0.6em; background-color: #fafaef;"
style2 = "margin: 0.8em 0px;padding: 0.6em;border-width: 1px;border-style: solid;border-color: rgb(192, 200, 209);border-radius: 0.3em;box-shadow: rgb(170, 170, 170) 0px 0px 0.6em;background-color: rgb(250, 250, 239);"
style3 ="padding: 0px; margin: 0px; border: none; color: rgb(51, 51, 51); font-size: 1em; line-height: 1.4em; word-break: break-all; word-wrap: break-word; background-image: none; font-family: inherit;"
Browser.get("http://weixin.sogou.com/weixin?query=%E4%B8%8A%E8%B4%A2%E8%A1%A8%E7%99%BD%E5%A2%99&_sug_type_=&s_from=input&_sug_=n&type=2&page=63&ie=utf8")
for p in range(63,70):
    #提取每页的10个
    this_page_biaobai = []
    for j in range(1,11):
        if p == 63:
            if j!= 4 or j != 7 or j != 8 or j != 10:
                continue
        Time = Browser.find_element_by_xpath("//ul[@class='news-list']/li[{}]/div[2]/div/span".format(j)).text
        gongzhonghao = Browser.find_element_by_xpath("//ul[@class='news-list']/li[{}]/div[2]/div/a".format(j)).text
        if "上财微生活" not in gongzhonghao:
            continue
        print(Time)
        year = int(Time[:4])
        if Time[6] == '-':
            month = int(Time[5])
        else:
            month = int(Time[5:7])
        if year < 2016 or (year == 2016 and month < 5):
            continue
        page_url = Browser.find_element_by_xpath("//ul[@class='news-list']/li[{}]/div[2]/h3/a".format(j)).click()
        time.sleep(0.5)
        for handle in Browser.window_handles:
            if handle != Browser.current_window_handle:
                Browser.close()
                Browser.switch_to.window(handle)
        raw_source = Browser.page_source
        PAGE = BeautifulSoup(raw_source,'html.parser')
        Time = PAGE.find_all(attrs={"id":"publish_time"})[0].text
        title = PAGE.find_all(attrs={"class":"rich_media_title"})[0].text.strip()[7:]
        year = int(Time[:4])
        month = int(Time[5:7])
        section = PAGE.find_all('section',attrs={"style":style1})
        if len(section) < 3:
            section = PAGE.find_all('section',attrs={"style":style2})
        if len(section) < 3 :
            section = PAGE.find_all('section',attrs={"style":style3})
        print(len(section))
        biaobai_page = []
        for one in section:
            text = one.find_all('span')
            if len(text)!=0:
                thisbiaobai = text[0].text.strip()
                maohao = thisbiaobai.index(":")
                biaobai  = thisbiaobai[maohao+1:]
                distinguish = True
                for i in range(len(biaobai_page)):
                    if biaobai_page[i] == biaobai:
                        distinguish = False
                if(distinguish):
                    biaobai_page.append(biaobai)
        print(biaobai_page)
        page_biaobao = (Time,title,biaobai_page)
        with open("{}.{}.txt".format(p,j),'wb+') as f:
            f.write(Time.encode('utf-8'))
            f.write('\n'.encode('utf-8'))
            f.write(title.encode('utf-8'))
            f.write('\n'.encode('utf-8'))
            for section in biaobai_page:
                f.write('[表白]'.encode('utf-8'))
                f.write('\n'.encode('utf-8'))
                f.write(section.encode('utf-8'))
                f.write('\n'.encode('utf-8'))
        Browser.get("http://weixin.sogou.com/weixin?query=%E4%B8%8A%E8%B4%A2%E8%A1%A8%E7%99%BD%E5%A2%99&_sug_type_=&s_from=input&_sug_=n&type=2&page={}&ie=utf8".format(p))

    time.sleep(5)
    next_page = Browser.find_element_by_id("sogou_next").click()
