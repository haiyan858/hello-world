# test_re.py
# _*_coding:utf-8_*_


# test = '用户输入的字符串'
# if re.match(r'正则表达式', test):
#     print('ok')
# else:
#     print('failed')
# re.match(r'^\d{3}[\s+|-]\d{3,8}$', '010-12345’)

# import re
# test = '010 2316858'

# if re.match(r'^\d{3}[\s+|_]\d{3,8}$',test):
# 	print('ok')
# else:
# 	print('failed')

# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com

import re

# ===================
def is_valid_email(addr):
	try:
		re_email = re.compile(r'(([a-zA-Z]+[.|#]?[a-zA-Z]+)@([a-zA-Z]+.com))')
	except Exception as e:
		print(e.message())
	else:
		return re_email.match(addr)

# 版本二可以提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob

def name_of_email(addr):
	re_addr = re.split(r'@', re_addr)[0]
	re.compile(r'^[<?|a-zA-Z+]\s[a-zA-Z]$')


	return None

# 第一题：
def is_valid_email(addr):
	if re.match(r'[a-zA-z_.]*@[a-aA-Z.]*',addr):
		return True
	else:
		return False

# 第二题：
def name_of_email(addr):
	r=re.compile(r'^(<?)([\w\s]*)(>?)([\w\s]*)@([\w.]*)$')
	if not r.match(addr):
		return None
	else:
		m=r.match(addr)
		return m.group(2)



# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')

assert not is_valid_email('mr-bob@example.com')
print('ok')

