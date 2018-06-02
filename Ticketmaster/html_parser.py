#!/usr/bin/env python
#-*-coding=utf8-*-

from bs4 import BeautifulSoup 
import re 
import urlparse
from selenium import webdriver
import time
import sys

class HtmlParser(object):
	def execute_times(self, times, url):
		driver = webdriver.Chrome()  # 用chrome浏览器打开
		driver.get("url")  # 打开知乎我们要登录
		time.sleep(2)
		for i in range(times + 1):
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(5)

	def parse_info(self, page_url, html):
		if page_url is None or html is None:
			return
		Ticketmaster = dict()
		Ticketmaster['myurl'] = page_url
		soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
		# 解析 观看项目名称
		try:
			title = soup.find('h1', attrs={'class': 'fl'})
			Ticketmaster['title'] = title.string
		except Exception as err:
			print '[warning][line:%s] parse date warning url=[%s] warning=[%s]' % (sys._getframe().f_lineno , page_url,err)
			return None
		# 解析场馆
		is_site = ''
		is_venve =''
		try:
			site = soup.find('div', attrs={'id': 'header'}).find('h2')
			is_site = site.get_text()
			venue = soup.find('li', attrs={'class': 'clearfix'}).find('a')
			is_venve = venue.get_text()
			Ticketmaster['site'] = is_site + ':' + is_venve
		except Exception as err:
			if is_site:
				Ticketmaster['site'] = is_site
			elif is_venve:
				Ticketmaster['site'] = is_venve
			else:
				Ticketmaster['site'] = u'暂无场馆信息'
			print '[warning][line:%s]parse site warning url=[%s], warning=[%s]' % (sys._getframe().f_lineno ,page_url,err)

		# 解析 日期/场次
		date_list = list()
		try:
			dates = soup.find('div', attrs={'class': 'date clearfloat'}).find_all('li')
			for date in dates:
				date_list.append(date.get_text())
			Ticketmaster['date_list'] = date_list
		except Exception as err:
			date_list.append(u'暂无日期信息')
			Ticketmaster['date_list'] = date_list
			print '[warning][line:%s] parse date warning url=[%s] warning=[%s]' % (sys._getframe().f_lineno ,page_url,err)

		# 解析票价信息
		price_set = set()
		price_data = list()
		try:
			prices_list = soup.find('ul', attrs={'class': 'date-ul price-ck price-l'})
			prices = prices_list.find_all('i')
			#去重
			for price in prices:
				wtf = price.get_text()
				price_set.add(wtf)
			#添加信息
			price_list = list(price_set)
			for value in price_list:
				value = str(value)
				price_data.append(value)
				price_data.append(u'元/场\n')
			Ticketmaster['price_list'] = price_data
		except Exception as	err:
			price_str = u'暂无票价信息'
			Ticketmaster['price_list'] = price_str
			print '[warning] [line:%s]parse price error url=[%s], warning=[%s]' % (sys._getframe().f_lineno,page_url, err)

		# 解析基本信息
		infos = soup.find('div', attrs={'id':'liveNav_1'}).find('div', attrs={'class': 'lives-info'})
		# 获取注意事项
		try:
			notes = infos.find('span', attrs={'class': 'fl'}).get_text()
			Ticketmaster['notes'] = notes
		except Exception as err:
			notes = u'暂无注意事项'
			Ticketmaster['notes'] = notes
			print '[warning][line:%s] parse notes warning url=[%s] warning=[%s]' % (sys._getframe().f_lineno ,page_url,err)

		# 获取演出详情
		try:
			show_info = infos.find('div', attrs={'class': 'lhg26'})
			if not show_info:
				Ticketmaster['info'] = None
				return Ticketmaster

			info_in_script = show_info.find('script')
			show_info_list = show_info
			if info_in_script:
				show_info_list = re.findall(r">(.*?)<", str(info_in_script))
			elif show_info:
				show_info_list =  re.findall(r">(.*?)<", str(show_info))
			Ticketmaster['info'] = show_info_list
		except Exception as err:
			show_info = u'暂无暂无详情信息'
			Ticketmaster['info'] = show_info
			print '[warning][line:%s]parse show_info warning url=[%s] warning=[%s]' % (sys._getframe().f_lineno ,page_url,err)

		return Ticketmaster

	def parse_home(self, page_url, html):
		if page_url is None or html is None:
			return
		soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
		divlinks = soup.find_all('a', attrs={'target': '_blank', 'href': re.compile(r'//www\.228.com\.cn/ticket-?')})
		count = 0
		url_list = list()
		for url in divlinks:
			count+=1
			url = str(url['href'])
			if url[0:6] == 'https:':
				url_list.append(url)
				print u'获取第[%s]个票务信息页面的url:[%s]' % (count,url)
				continue
			url = url.replace('//','https://')
			url_list.append(url)
			print u'获取第[%s]个票务信息页面的url:[%s]' % (count,url)
		return url_list
