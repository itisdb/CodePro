def transpose(matrix):
	for i in range(len(matrix)):
		for j in range(i, len(matrix[i])):
			temp = matrix[i][j]
			matrix[i][j]=matrix[j][i]
			matrix[j][i]=temp
	return matrix

def reverse(matrix):
	for i in range(len(matrix)):
		matrix[i] = (matrix[i])[::-1]
	return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(reverse(transpose(matrix)))