list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def composable(l: list, k:int):
	it_count = 0
	copy = l.copy()
	for a in l:
		for b in l:
			it_count += 1
			if a != b and a + b == k:
				print("match found: " + str(a) + " + " + str(b) + " = " + str(k))
				print("in list: " + str(copy))
				print("after " + str(it_count) + " iterations")
				return True
		l.pop(0)
	print("no match found")
	return False
	

composable(list, 19)

