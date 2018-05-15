# -*- coding: utf-8 -*-

# 2.2 编写程序，生成包含1000个0到100之间的随机整数，并统计每个元素的出现次数。（提示：使用集合。）

import random

random_list = []

while len(random_list)<1000:
	random_list.append(int(random.random()*100))

# print random_list
# print random_list.count()

