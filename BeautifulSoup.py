#!/usr/bin/env python
#-*-coding=utf8-*-

from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<div class="para" label-module="para">在计算机科学中<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
</div><a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#创建解析html的soup对象
soup = BeautifulSoup( html_doc,                #HTML文档
					  'html.parser',	   #HTML解释器
					  from_encoding='utf-8' #HTML文档使用的编码
					)



# 搜索节点标签方法 find_all/find(name,attrs,string)
#node = soup.find_all('a',class_='abc',string='python') #class加下划线是为了区别关键字
#node.name   #获取你标签名字
#name['href']#以字典的形式访问href属性的值
#node.get_text()#获取节点中的链接文字

print '获取所有链接'
node = soup.find_all('a')
print 'node',node
for link in node:
	print link.name, link['href'], link.get_text()


print '获取指定url链接'
node_link = soup.find('a', class_='sister')
print node_link.name, node_link['href'], node_link.get_text()


print '使用正则表达进行模糊匹配'
node = soup.find('div', class_='para').find_all('a', href=re.compile('exa'))
for node_link in node:
	print node_link.name, node_link['href']
	print node_link.get_text()


#1、compile()

#编译正则表达式模式，返回一个对象的模式。（可以把那些常用的正则表达式编译成正则表达式对象，这样可以提高一点效率。）

#格式：

#re.compile(pattern,flags=0)

#pattern: 编译时用的表达式字符串。

#flags 编译标志位，用于修改正则表达式的匹配方式，如：是否区分大小写，多行匹配等。常用的
