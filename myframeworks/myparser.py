def av2bv(av):
	"""av号转bv号
	:param av: av号
	:return: bv号
	"""
	return MyParser.bv2av(av)


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
		bv = (av ^ MyParser._XOR) + MyParser._OFFSET
		mask = list("BV1  4 1 7  ")
		for i, order in enumerate(MyParser._ORDERS):
			const = len(MyParser._TABLE) ** i
			mask[order] = MyParser._TABLE[bv // const % len(MyParser._TABLE)]
		return "".join(mask)

	@staticmethod
	def bv2av(bv):
		dic = {t: i for i, t in enumerate(MyParser._TABLE)}
		items = ((dic[bv[order]] * len(MyParser._TABLE) ** i) for i, order in enumerate(MyParser._ORDERS))
		return (sum(items) - MyParser._OFFSET) ^ MyParser._XOR
