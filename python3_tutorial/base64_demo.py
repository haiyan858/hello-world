# -*- coding: utf-8 -*-
# 2018年 1月31日 星期三 15时33分17秒 CST

# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
# 因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
# 因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。


# 练习
# 请写一个能处理去掉=的base64解码函数：
import base64

def safe_base64_decode(s):
	# 判断传入参数的类型
	if type(s) is bytes:
		s = str(s, encoding='utf-8')
	# 字符串的长度变为4的倍数
	s = s+str((4-len(s)%4)*'=')
	return base64.b64decode(s)



# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')


