def mergeOverlapping(matrix):
	matrix=sorted(matrix)
	res = []
	for i in range(1,len(matrix)):
		if (matrix[i-1])[1]>(matrix[i])[0]:
			res.append([(matrix[i-1])[0],(matrix[i])[1]])
		else:
			if i==0:
				res.append(matrix[i-1])
				res.append(matrix[i])
			else:
				res.append(matrix[i])
	return res

matrix = [[1,3],[2,6],[8,10],[15,18]]
print(mergeOverlapping(matrix))