

#recursive

def fibonacci(n):
	"""generates the nth digit of the fibonacci sequence"""
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)




#iterative
def fib_sequence(n):
	"""generates the nth digit of the fibonacci sequence"""
	x = 0
	y = 1
	for i in range(1,n):
		i = x + y
		x,y = y, i
	return y


if __name__=='__main__':
	print(fibonacci(10))
	print(fib_sequence(10))
