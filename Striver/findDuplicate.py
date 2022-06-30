def findDuplicate(matrix):
	dic = {k:0 for k in matrix}
	for i in matrix:
		dic[i]+=1
	for i in dic.keys():
		if dic[i]>1:
			print(str(i))

matrix = [1,3,4,2,2]
(findDuplicate(matrix))
