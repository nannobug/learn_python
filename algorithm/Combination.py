# list all combination of k elements choosing from n elements
def combination(n,k):
	ls = []
	if k == 1:
		for i in range(1,n+1):
			ls.append([i])
		return ls
	elif k > 1:
		ls_old = combination(n,k-1)
		for i in range(1,n-k+2):
			for f in ls_old:
				if i < f[-1]:
					ls.append(f+[i])
	return ls

print(combination(10,4))