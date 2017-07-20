
def fib(count, c, a, b, length):
	if count > length:
		return
	if count <= length:
		print c,
		c = a + b
		fib(count+1, c, b, c, length)

if __name__ == '__main__':
	fib(1, 0, 1, 0, 10)
