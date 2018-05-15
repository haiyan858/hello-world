#!/bin/use/env python
# _*_ coding:urf-8 _*_

# 2018年 1月15日 星期一 17时00分00秒 CST

# 练习2: 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os
def search_file(dir_path, name):
	for p in os.listdir(dir_path):
		fp = os.path.join(dir_path, p)
		if os.path.isdir(fp):
			search_file(fp, name)
		elif os.path.isfile(fp) and name in p:
			# print('匹配到文件：%s' % fp)
			print(os.path.dirname(fp)) # 相对路径



search_file('/Users/cuihaiyan/workInZebra/hotelSystemPro_V2','test')

