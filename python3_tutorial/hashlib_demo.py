# -*- coding: utf-8 -*-
# 2018年 2月 1日 星期四 16时10分08秒 CST

# 练习1
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：


import hashlib


db = {
	'michael': 'e10adc3949ba59abbe56e057f20f883e',
	'bob': '878ef96e86145580c38c87f0410ad153',
	'alice': '99b1c2188db85afee403b1536010c2c9'
}


def calc_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()


def login(user, password):
	if user in db.keys():
		if db[user] == calc_md5(password):
			return True
	return False



assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

