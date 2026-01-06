def has_digit(n, k):
	"""
	Returns whether k is a digit in n.
	>>> has_digit(10, 1)
	True
	>>> has_digit(12, 7)
	>>> False
	"""
	assert k >= 0 and k < 10, 'k must be a single digit.'
	while n >= 0:
		if n % 10 == k:
			return True
		elif n < 10 and n != k:
			break
		n = n // 10
	return False

def unique_digits(n):
	"""
	Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
	3
	>>> unique_digits(101) # 0 and 1
	2
	"""
	factor = 0
	count  = 0
	while factor < 10:
		if has_digit(n, factor):
			count += 1
		factor += 1
	return count