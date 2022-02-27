def stock(matrix):
	maxVal = 0
	for i in range(len(matrix)-1):
		if max(matrix[i+1:])>matrix[i]:
			diff = max(matrix[i+1:])-matrix[i]
			if diff>maxVal:
				maxVal=diff
	return maxVal

matrix = [7,1,5,3,6,4]
print(stock(matrix))