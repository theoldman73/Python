def myfunc(n):
	return lambda i: i*n
doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " +str(tripler(val)))
