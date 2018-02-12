#!/usr/bin/env python
# -*_coding:utf8-*-

import urllib2
import cookielib

url = 'http://www.baidu.com'

print 'first methond'
response1 = urllib2.urlopen(url)
print response1.getcode() #请求状态码
print len(response1.read()) #read爬取网页信息


print 'second methond'
request = urllib2.Request(url) #生成一个请求对象
request.add_header('user-agent','Mozilla/5.0') #在请求对象里添加请求头部信息
response2 = urllib2.urlopen(request)
print response2.getcode() #请求状态码
print len(response2.read()) #read爬取网页信息


print 'third method'
cj = cookielib.CookieJar() #创建一个cookie容器对象
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) #创建一个具有HTTPcookieProcessor方法的opener对象
urllib2.install_opener(opener) #给urllib2安装这个opener，urllib2就有了cookie处理的能力
response3 = urllib2.urlopen(url)
print response3.getcode() #请求状态码
print response3.read() #read爬取网页信息
