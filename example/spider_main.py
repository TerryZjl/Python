#!/usr/bin/env python
#-*-coding=utf8-*-

import url_manager
import html_output
import html_parser
import html_downloader

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()               #url管理器
		self.downloader = html_downloader.HtmlDownloader() #网页下载器
		self.parser = html_parser.HtmlParser()             #解析器
		self.output = html_output.HtmlOutput()			   #结果输出器  

	def craw(self, root_url): #爬虫的调度程序
		count = 1
		self.urls.add_new_url(root_url)   #添加初始的url
		while  self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()#从url管理起中获取一个待爬取url
				print u'爬取第[%d]个url: %s' % (count, new_url)
				html_cont = self.downloader.download(new_url) 
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls) #将新的url添加到url管理器
				self.output.collect_data(new_data) #输出器收集数据
				if count == 100:
					break
				count = count + 1 
			except:
				print 'craw error'
		self.output.output_html() #将结果输出

if __name__=='__main__':
	#root_url = 'https://baike.baidu.com/view/21087.htm'
	root_url = 'https://baike.baidu.com/item/%E6%8C%87%E9%92%88'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)

	
		
