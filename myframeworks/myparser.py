table = "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF"
orders = [11, 10, 3, 8, 4, 6]
xor = 177451812
offset = 8728348608


def bv2av(bv):
	dic = {t: i for i, t in enumerate(table)}
	items = ((dic[bv[order]] * len(table) ** i) for i, order in enumerate(orders))
	return (sum(items) - offset) ^ xor


def av2bv(av):
	bv = (av ^ xor) + offset
	mask = list("BV1  4 1 7  ")
	for i, order in enumerate(orders):
		const = len(table) ** i
		mask[order] = table[bv // const % len(table)]
	return "".join(mask)
