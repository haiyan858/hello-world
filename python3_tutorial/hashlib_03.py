#!/usr/bin/python3
# -*- coding: utf-8 -*-


# key:登录的用户名
# value1: 登录时的密码
# value2:初始化的key值

import hmac, random


class User(object):
	def __init__(self, username, password):
		self.username = username
		self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
		self.password = hmac_md5(self.key, password)

db = {}

def hmac_md5(key, s):
	return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

def register(username, password):
	db[username] = User(username, password)
	return True

def login(username, password):
	user = db[username]
	return user.password == hmac_md5(user.key, password)


assert register('michael', '123456')
assert register('bob', 'abc999')
assert register('alice', 'alice2008')
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
print(db)

