import urllib.request
import http.cookiejar
from xml.etree import ElementTree
import os
import time
import ctypes

url = 'https://www.bing.com/HPImageArchive.aspx?format=rss&idx=0&n=1&mkt=en-US'

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path) 

    return True

# 方法一
# print('方法一')
req_one = urllib.request.Request(url)
req_one.add_header('User-Agent', 'Mozilla/6.0')
res_one = urllib.request.urlopen(req_one)
code_one = res_one.getcode()
html_one = res_one.read().decode('utf-8')
res_one.close()
#print('方法一网页状态码：%s' % (code_one))
#print('方法一网页内容：'+html_one)
tree = ElementTree.fromstring(html_one)
link = tree.iter("link")
'''
print(links[index])
print(type(links[index]))
print(links[index].tag)#获取<a>标签名a
print(links[index].attrib)#获取<a>标签的属性href和class
print(links[index].text)#获取<a>标签的文字部分
输出：
<Element a at 0x3866a58>
<class 'lxml.etree._Element'>
a
{'href': 'magnet:?xt=urn:btih:7502edea0dfe9c2774f95118db3208a108fe10ca', 'class': 'download'}
磁力链接
'''
tmpbing=next(link).text
tmppicurl=next(link).text
picurl1=tmpbing.split('/')
picurl2=''
#print (type(picurl1))
for i in range(len(picurl1)-1):
    #print ("%s/" % (picurl1[i]),end='')
    picurl2+=picurl1[i]+'/'

picurl=picurl2+tmppicurl.strip('/')

username = os.popen('whoami').read().split('\\')[1].strip('\n')
localpath="C:\\Users\\"+ username +"\\Pictures\\Bing"
mkdir(localpath)
now=time.strftime("%Y-%m-%d", time.localtime())
localpicfullpath=localpath + "\\" + now + ".png"

urllib.request.urlretrieve(picurl, localpicfullpath)

ctypes.windll.user32.SystemParametersInfoW(20, 0, localpicfullpath, 0)      
'''
# 方法二
print('方法二')
res_two = urllib.request.urlopen(url)
code_two = res_two.getcode()
html_two = res_two.read().decode('utf-8')
print('方法二网页状态码：%s' % (code_two))
print('方法二网页内容：'+html_two)
 
 
#方法三
print('方法三')
cj = http.cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
res_three = urllib.request.urlopen(url)
print(cj)
code_three = res_three.getcode()
html_three = res_three.read().decode('utf-8')
res_three.close()
print('方法三网页状态码：%s' % (code_three))
print('方法三的网页内容：'+html_three)
'''


