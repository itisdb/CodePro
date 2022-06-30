def repeatingMissing(matrix):
	matrix = sorted(matrix)
	for i in range(1,len(matrix)):
		if matrix[i]-matrix[i-1]>1:
			print((str(matrix[i]-1)+" "),end="")
		if matrix[i]==matrix[i-1]:
			print(str(matrix[i]))

matrix = [3,1,2,5,3]
repeatingMissing(matrix)
