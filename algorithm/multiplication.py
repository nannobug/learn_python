# assume x, y have same number of digits
def mul(x,y):
	n = len(str(x))
	a = x//(10**(n//2))
	b = x%(10**(n//2))
	c = y//(10**(n//2))
	d = y%(10**(n//2))
	if n == 1:
		return x*y
	mul(a,c)
	mul(a,d)
	mul(b,c)
	mul(b,d)
	return (10**n)*a*c+10**(n//2)*(a*d+b*c)+b*d
print(mul(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
	