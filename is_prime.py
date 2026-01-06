def is_prime(n):
	"""
	>>> is_prime(10)
	False
	>>> is_prime(7)
	True
	>>> is_prime(1) # one is not a prime number!!
	False
	"""
	factor = 2
	while factor < n:
		if n % factor == 0 or n <= 1:
			return False
		factor += 1
	return True