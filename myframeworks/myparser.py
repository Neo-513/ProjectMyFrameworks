_TABLE = "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF"
_ORDERS = [11, 10, 3, 8, 4, 6]
_XOR = 177451812
_OFFSET = 8728348608


def bv2av(bv):
	dic = {t: i for i, t in enumerate(_TABLE)}
	items = ((dic[bv[order]] * len(_TABLE) ** i) for i, order in enumerate(_ORDERS))
	return (sum(items) - _OFFSET) ^ _XOR


def av2bv(av):
	bv = (av ^ _XOR) + _OFFSET
	mask = list("BV1  4 1 7  ")
	for i, order in enumerate(_ORDERS):
		const = len(_TABLE) ** i
		mask[order] = _TABLE[bv // const % len(_TABLE)]
	return "".join(mask)
