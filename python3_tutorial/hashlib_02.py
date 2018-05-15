# -*- coding: utf-8 -*-
# 2018年 2月 1日 星期四 16时14分08秒 CST

# 练习2
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

# -*- coding: utf-8 -*-
import hashlib, random


def get_md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
	def __init__(self, username, password):
		self.username = username
		self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
		self.password = get_md5(password + self.salt)


db = {}
def register(username, password):
	db[username] = User(username, password)
	return True

def login(username, password):
	# 对象 User=db[username] 有三个属性：
	# db[username].password
	# db[username].salt
	# db[username].username
	user = db[username]
	return user.password == get_md5(password + user.salt)

register('michael', '123456')
login('michael', '123456')



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




