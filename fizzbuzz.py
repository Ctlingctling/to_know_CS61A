def fizzbuzz(n):
	"""
	>>> result = fizzbuzz(16)
	1
	2
	fizz
	4
	buzz
	fizz
	7
	8
	fizz
	buzz
	11
	fizz
	13
	14
	fizzbuzz
	16
	>>> print(result)
	None
	"""
	count = 0
	while count <= n:
		if   count % 3 == 0 and count % 5 != 0:
			print("fizz")
		elif count % 3 != 0 and count % 5 == 0:
			print("buzz")
		elif count % 15 == 0:
			print("fizzbuzz")
		else:
			print(count)
		count += 1