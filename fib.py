
def fib(count, third, first, second, length):
	if count > length:
		return
	if count <= length:
		print third,
		third = first + second
		fib(count+1, third, second, third, length)

if __name__ == '__main__':
	fib(1, 0, 1, 0, 10)
