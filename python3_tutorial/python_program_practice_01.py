# python_program_practice_01.py
# -*- coding: utf-8 -*-

# 编写程序，用户输入一个三位以上的整数，输出其百位以上的数字。例如用户输入1234，则程序输出12。（提示：使用整除运算。）

# num = input("输入一个三位以上的整数:")

# if len(num) >3:
# 	# print(num)
# 	print(int(int(num)/100))


# 标准答案

x = input('Please input an integer of more than 3 digits:')
try:
	x = int(x)
	x = x//100
	if x == 0:
		print('You must input an integer of more than 3 digits.')
	else:
		print(x)
except BaseException:
	print('You must input an integer.') 

