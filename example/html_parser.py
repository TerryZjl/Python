#!/usr/bin/env python
#-*-coding=utf8-*-

from bs4 import BeautifulSoup 
import re 
import urlparse

class HtmlParser(object):
	
	def _get_new_urls(self, page_url, soup): #获取当前页面里有用的链接
		new_urls = set()
		divlinks = soup.find_all('div',class_='para')
		print 'craw new url'
		for divlink in divlinks:
			links = divlink.find_all('a', href=re.compile(r"item"))
			for link in links:
				new_url = link['href'] #匹配出href后面对应的字符串
				new_full_url = urlparse.urljoin(page_url, new_url)#urlparse的urljoin放法是把new_url按照page_url的格式链接在page_url上
				new_urls.add(new_full_url)
				print new_full_url
		print 'craw end'
		return new_urls


	def _get_new_data(self, page_url, soup): #获取当前页面有用的数据
		res_data = {} #存放数据的字典
		#把当前url收集起来
		res_data['url'] = page_url
		
		#收集关键词条<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
		title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
		res_data['title'] = title_node.get_text()
		#收集词条对应解释信息<div class="lemma-summary" label-module="lemmaSummary">
		summary_node = soup.find('div',class_='lemma-summary')
		res_data['summary'] = summary_node.get_text()
		
		return res_data
		
	def parse(self, page_url, html):
		if page_url is None or html is None:
			return
		soup = BeautifulSoup(html, 'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(page_url, soup)
		return new_urls, new_data

