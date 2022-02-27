def find(matrix):
	zeroes = 0
	ones = 0
	twos = 0
	for i in matrix:
		if i == "0" or i == 0:
			zeroes+=1
		elif i == "1" or i == 1:
			ones+=1
		elif i == "2" or i == 2:
			twos+=1
	matrix = [0]*zeroes
	matrix.extend([1]*ones)
	matrix.extend([2]*twos)
	print(matrix)

matrix = [0,1,0,2,2,0,1,0,2,1]
find(matrix)