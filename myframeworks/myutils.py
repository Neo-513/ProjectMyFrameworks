import time


def jsn2dic(jsn):
	"""将json字符串转为json字典
	:param jsn: 待转换json字符串
	:return: 转换后的json字典
	"""
	if isinstance(jsn, dict):
		return jsn
	elif isinstance(jsn, str):
		return eval(jsn.replace("null", "None").replace("true", "True").replace("false", "False"))


def timing(func):
	"""统计函数执行时间
	:param func: 待执行函数
	:return: 装饰器函数
	"""
	def inner(*args):  # 内部函数
		tictoc = time.time()
		datas = func(*args)  # 执行函数
		print(f"{func.__name__}():    {time.time() - tictoc}")
		return datas
	return inner


def av2bv(av):
	"""av号转bv号
	:param av: av号
	:return: bv号
	"""
	return MyParser.av2bv(av)


def bv2av(bv):
	"""bv号转av号
	:param bv: bv号
	:return: av号
	"""
	return MyParser.bv2av(bv)


class MyParser:
	_TABLE = "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF"
	_ORDERS = [11, 10, 3, 8, 4, 6]
	_XOR = 177451812
	_OFFSET = 8728348608

	@staticmethod
	def av2bv(av):
		av = int(av)
		bv = (av ^ MyParser._XOR) + MyParser._OFFSET
		mask = list("BV1  4 1 7  ")
		for i, order in enumerate(MyParser._ORDERS):
			mask[order] = MyParser._TABLE[bv // len(MyParser._TABLE) ** i % len(MyParser._TABLE)]
		return "".join(mask)

	@staticmethod
	def bv2av(bv):
		dic = {t: i for i, t in enumerate(MyParser._TABLE)}
		items = ((dic[bv[order]] * len(MyParser._TABLE) ** i) for i, order in enumerate(MyParser._ORDERS))
		return (sum(items) - MyParser._OFFSET) ^ MyParser._XOR
