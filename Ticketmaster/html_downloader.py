#!/usr/bin/env python
#-*-coding=utf8-*-

import urllib2
from selenium import webdriver
import time

class HtmlDownloader(object):
	def download(self,url):
		try:
			myheaders = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
			req = urllib2.Request(url, headers=myheaders)
			response = urllib2.urlopen(req)

			if response.getcode() != 200:
				return None
			return response.read()
		except Exception as err:
			print 'download url=[%s] error [%s]' % (url,err)
	def download_driver(self,url,num):
		try:
			driver = webdriver.Chrome()  # 用chrome浏览器打开
			driver.get(url)  # 打开知乎我们要登录
			print '打开网页，请稍等等...'
			time.sleep(2)
			page_num = num/20 + 1
			for i in range(page_num):
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				print '加载第[%s]个网页，请稍等等...' % (i+1)
				time.sleep(5)
			new_html = driver.page_source
			return new_html
		except Exception as err:
			print 'download_driver error [%s]' % (err)
