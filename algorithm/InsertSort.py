def InsertSort(array):
	for i in range(1,len(array)):
		j = i-1
		#print("j=",j)
		while j >= 0 and array[j] > array[i]:
			s = array[i] + array[j]
			array[j] = s - array[j]
			array[i] = s - array[j]
			#print("j=", j, "a_j=",array[j])
			#print("i=", i,"a_i=",array[i])
			i -= 1
			j -= 1			
	return array
print(InsertSort([1,2,6,7,4,2]))