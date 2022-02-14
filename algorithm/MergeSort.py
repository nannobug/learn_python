def MinSort(ls):
	n = len(ls)
	i = 0
	output = []
	while n > 0:
		m = min(ls)
		ls.remove(m)
		output.append(m)
		n -= 1
	return output

def MergeSort(ls):
	if len(ls) <= 1:
		return ls
	output = [[],[]]
	inv = 0
	# break an array in to two arrays
	L = ls[0:len(ls)//2]
	R = ls[len(ls)//2:]
	#sort each array
	L = MergeSort(L)
	R = MergeSort(R)
	#merge the sorted arrays
	i, j = 0, 0
	while i < len(L) or j < len(R):
		if i == len(L) or j == len(R):
			if i == len(L):
				output[1] = output[1] + R[j:]
			else:
				output[1] = output[1] + L[i:]
			output[2] = [inv]
			return output
		else:
			if L[i] > R[j]:
				output.append(R[j])
				j += 1
				output[2] = [inv + len(L)]
			else:
				output.append(L[i])
				i += 1
	return output

print(MergeSort([9,0,2,3,3,1]))
