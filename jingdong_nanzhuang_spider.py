'''March 16,2018 Author: Zhiying Zhou'''
import requests
from requests.exceptions import RequestException
from urllib.request import urlretrieve
import re
from multiprocessing import Pool
import time


# 获取网页
def get_Html_Page(url):
    try:
        r = requests.get(url,headers = {"User-Agent":"Moziall/5.0"})
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except RequestException:
        print(RequestException)
        
        
# 提取网页的图片的网址
def parse_Html_Page(html):
    pattern1 = '<img width="220" height="282" class="err-product" data-img="1" src="//(.*?\.jpg)" />'
    pattern2 = '<img width="220" height="282" class="err-product" data-img="1" data-lazy-img="//(.*?\.jpg)" />'
    list = []
    list = re.findall(pattern1,html) + re.findall(pattern2,html)
    return list
    
    
# 以页为单位下载图片并保存到本地
def download(list,index):
    for i in range(len(list)):
        uri = "https://" + str(list[i])
        path = "D:\\Demos\\jingdong\\" + "第" + str(index) + "页" + str(i) +".jpg"
        urlretrieve(uri,filename=path)
        
        
def main(index):
    # 构造网址
    url = "https://search.jd.com/Search?keyword=男装&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=男装&cid2=1342&page=" + \
          str(index * 2 + 1)
    print("正在获取第%s页》》》" % index)
    get_Html_Page(url)
    html = get_Html_Page(url)
    parse_Html_Page(html)
    list = parse_Html_Page(html)
    download(list,index)
    print("第%s页获取成功！" % index)
    
    
if __name__== '__main__':
    time.clock()
    p = Pool()
    p.map(main,(index for index in range(100)))
    print("获取图片成功！\n")
    print("程序运行时间为{}".format(time.clock()))




