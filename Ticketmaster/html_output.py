#!/usr/bin/env python
#-*-coding=utf8-*-

import xlwt
import gc
gc.collect()
class HtmlOutput(object):
	def __init__(self):
		self.new_table = 'mydata.xls'
		self.wb = xlwt.Workbook(encoding='utf-8')
		self.ws = self.wb.add_sheet('sheet1')
		headData = [u'剧名',u'票价',u'日期',u'地点',u'演出详情',u'注意事项',u'购票链接']
		for colnum in  range(0,7):
			self.ws.write(0,colnum,headData[colnum],xlwt.easyxf('font: bold on'))

	def output_execl(self,count, data):
		if data is None:
			return
		self.ws.write(count, 0, data['title'], xlwt.easyxf('font: bold on'))
		price_str = ''.join(data['price_list'])
		self.ws.write(count, 1,price_str, xlwt.easyxf('font: bold on'))
		date_str = ''.join(data['date_list'])
		self.ws.write(count, 2, date_str, xlwt.easyxf('font: bold on'))
		self.ws.write(count, 3, data['site'], xlwt.easyxf('font: bold on'))
		if data['info'] is None:
			self.ws.write(count, 4, u'暂无详情信息', xlwt.easyxf('font: bold on'))
		else:
			self.ws.write(count, 4, data['info'], xlwt.easyxf('font: bold on'))
		self.ws.write(count, 5, data['notes'], xlwt.easyxf('font: bold on'))
		self.ws.write(count, 6, data['myurl'], xlwt.easyxf('font: bold on'))

	def Save(self):
		self.wb.save(self.new_table)
