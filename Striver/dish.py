def dish(matrix):
	dic = { _:[] for _ in matrix}
	start = 0
	for i in range(1,len(matrix)):
		if matrix[i]!=matrix[i-1]:
			dic[matrix[i-1]].append(matrix[start:i])
			start=i
	if start!=len(matrix)-1:
		dic[matrix[start]].append(matrix[start:len(matrix)])
	print(dic)

matrix = [1,2,2,1,2,1,1,1,1]
dish(matrix)