import math

def merge(matrix, matrix2):
	n=len(matrix)
	m=len(matrix)
	gap = int(math.ceil((len(matrix)+len(matrix2))/2.0))
	while (gap>0):
		i=0
		j=gap
		while j<(n+m):
			if j<n and matrix[i]>matrix[j]:
				temp=matrix[i]
				matrix[i]=matrix[j]
				matrix[j]=temp
			elif j>=n and i<n and matrix[i]>matrix2[j-n]:
				temp=matrix[i]
				matrix[i]=matrix2[j-n]
				matrix2[j-n]=temp
			elif j>=n and i>=n and matrix2[i-n]>matrix2[j-n]:
				temp=matrix2[i-n]
				matrix2[i-n]=matrix2[j-n]
				matrix2[j-n]=temp
			j+=1
			i+=1
		if gap==1:
			gap=0
		else:
			gap=int(math.ceil(gap/2.0))

	print(matrix)
	print(matrix2)


matrix = [1,4,7,8,10]
matrix2 = [2,3,9]
merge(matrix,matrix2)