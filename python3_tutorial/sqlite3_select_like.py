#!/usr/bin/env python
# _*_coding:utf-8_*_

# 请编写函数，在Sqlite中根据分数段查找指定的名字：

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low,high):
	# ' 返回指定分数区间的名字，按分数从低到高排序 '
	try:
		conn = sqlite3.connect('test.db')
		cursor = conn.cursor()
		# 执行查询语句:
		cursor.execute('select * from user where ?<= score and score <=? order by score asc',(low,high))
		# 获得查询结果集:
		values = cursor.fetchall()
	except Exception as e:
		print(e)
	else:
		print('conn is ok ')
	finally:
		cursor.close()
		conn.close()	
	return [i[1] for i in values]

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')

