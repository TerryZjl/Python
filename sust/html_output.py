#!/usr/bin/env python
#-*-coding=utf8-*-

class HtmlOutput(object):
	def __init__(self):
		self.datas = [] #初始一个存放收集数据的列表

	def collect_data(self,data): #收集解析来的数据
		if data is None:
			return
		for num in data:
			self.datas.append(num)

	def output_html(self): #将收集的数据放入html文件中
		fout = open('output.html','w')

		fout.write("<html>")
		fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
		fout.write("<body>")
		fout.write("<table>")
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>" % data['company'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['link'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['local'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['time'].encode('utf-8'))
			fout.write("</tr>")
		
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")

		fout.close()
