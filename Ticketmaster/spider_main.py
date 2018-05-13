#!/usr/bin/env python
#-*-coding=utf8-*-

import url_manager
import html_output
import html_parser
import sys
import html_downloader


class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()               #url管理器
		self.downloader = html_downloader.HtmlDownloader() #网页下载器
		self.parser = html_parser.HtmlParser()             #解析器
		self.output = html_output.HtmlOutput()			   #结果输出器  

	def craw_city(self,root_url,num):
		try:
			html = self.downloader.download_driver(root_url,num)
			urls = self.parser.parse_home(root_url,html)

			self.urls.add_new_urls(urls)  # 将新的url添加到url管理器,方便扩展使用多线程进行爬取
			count = 0
			for url in urls:
				if count >= num:
					break
				count +=1
				part_html = self.downloader.download(url)
				data = self.parser.parse_info(url, part_html)
				self.output.output_execl(count, data)
		except Exception as err:
			print u'票务信息爬取出错'
			self.output.Save()
			print '[warning] [line:%s]parse price error url=[%s], warning=[%s]' % (sys._getframe().f_lineno, page_url, err)
		finally:
			print u'票务信息爬取结束'
			self.output.Save()

if __name__=='__main__':
	root_url='https://www.228.com.cn/category/'
	obj_spider = SpiderMain()
	num = 0
	while num <= 0:
		num = int(raw_input("设置爬要取多少条票务信息:>"))
	obj_spider.craw_city(root_url,num)

	
		
