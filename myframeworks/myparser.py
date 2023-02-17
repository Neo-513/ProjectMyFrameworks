chars = "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF"
idxs = [11, 10, 3, 8, 4, 6]
xor = 177451812
oft = 8728348608


def bv2av(bv):
	tr = {char: i for i, char in enumerate(chars)}
	items = [(tr[bv[idx]] * len(chars) ** i) for i, idx in enumerate(idxs)]
	return (sum(items) - oft) ^ xor


def av2bv(av):
	bv = (av ^ xor) + oft
	mask = list("BV1  4 1 7  ")
	for i, idx in enumerate(idxs):
		const = len(chars) ** i
		mask[idx] = chars[bv // const % len(chars)]
	return "".join(mask)

print(bv2av('BV1JK411p7pd'))
print(av2bv(498461045))

print(bv2av('BV1i4411k7KW'))
print(av2bv(66897596))




print(av2bv(844433045))
#498461045
#BV1JK411p7pd