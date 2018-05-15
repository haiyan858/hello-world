# -*- coding:utf-8 -*-
# 2018年 01月 31日 星期三 10:01:37 CST

# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
	# tz_utc = timezone(timedelta(hours=int(tz_str[3:].split(':')[0]))) # 时区UTC+8:00
	# 正则匹配时区信息
	# tz = re.match(r'[+|-]+\d+',tz_str)
	tz = re.match(r'UTC([+\-]\d+):00', tz_str).group(1)
	tz_utc = timezone(timedelta(hours=int(tz)))
	#转化为时间格式
	cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	cday_tz_utc = cday.replace(tzinfo=tz_utc)
	return cday_tz_utc.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

