# Question: does array A contain integer t
def oneloop(array, t):
	for i in range(len(array)):
		if array[i] == t:
			return True
	return False
#O(n)
#print(oneloop([1,2,3,4],0))

# Question: Does array A,B have a number in common:
def TwoLoop(A, B):
	for a in A:
		for b in B:
			if a == b:
				return True
	return False
#print(TwoLoop([1,2,3], [1,3]))
#O(x**2)

# Question: does A has duplicate?
def duplicate(A):
	for i in range(len(A)-1):
		for j in range(i+1,len(A)):
			if A[i] == A[j]:
				return True
	return False
#O(n**2)
#print(duplicate([1,2,3,4,5]))