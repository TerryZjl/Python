#!/usr/bin/env python2.6
#-*-coding:utf8-*-

import codecs
import requests
from bs4 import BeautifulSoup


URL = 'https://movie.douban.com/top250'

def Download_Page(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
	}
	data = requests.get(url, headers=headers).content
	return data

def parse_html(html):

	soup = BeautifulSoup(html)
	
	movie_name_list = []
	movie_list_soup = soup.find('ol',attrs={'class':'grid_view'})
	for movie_li in movie_list_soup.find_all('li'):
	
		detail = movie_li.find('div',attrs={'class':'hd'})
		movie_name = detail.find('span',attrs={'class':'title'}).getText()
		movie_name_list.append(movie_name)
		
	next_page = soup.find('span',attrs = {'class':'next'}).find('a')
	if next_page:
		return movie_name_list, URL+next_page['href']
	return movie_name_lsit, None


def main():
	url = URL
	i=0
	while url:
		html = Download_Page(url)
		movies, url = parse_html(html)
		for movie in movies:
			i+=1
			print i, movie
	


	

#__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行
if __name__ == '__main__':
	main()
