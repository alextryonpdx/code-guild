
def fib(n):
	a = n-1
	b = n-2
	n = fib(a) - fib(b)
	print n

fib(10)



"""
def find_fibs(n):
	
	if n == 0:
		return n
	if n == 1:
		return n
	else:
		n = (find_fibs(n - 1) + find_fibs(n - 2))
	print n


n = int(raw_input("n is"))
find_fibs(n)
print n
"""
"""
def fib(a):
	if a > 1:
		a = fib((a-1)) + fib((a-2))
		print a
	else:
		print a

	

fib(10)
"""