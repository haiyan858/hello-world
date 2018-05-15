# class_and_instance_07.py

# class Loaf(object):
# 	"""docstring for Loaf
# 	# Python 类的确存在与构造函数相似的东西
# 	"""
# 	def __init__(self, arg):
# 		super(Loaf, self).__init__()
# 		self.arg = arg
# 	pass

from UserDict import UserDict

# class FileInfo(UserDict):
# 	# """docstring for FileInfo"""
# 	# def __init__(self, arg):
# 	# 	super(FileInfo, self).__init__()
# 	# 	self.arg = arg
# 	def __init__(self,fileName=None):

# 		pass

class FileInfo(UserDict):
	# "store file metadata"
	def __init__(self, filename=None):
		UserDict.__init__(self)
		self["name"] = filename
