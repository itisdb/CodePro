def cuteCat(matrix, string):
	res=[]
	for i in matrix:
		if i in string:
			res.append("Yes")
		else:
			res.append("No")
	return res

matrix = ["cute cat", "ttle", "cutest", "dog", "c++", "big"]
string = "little cute cat loves to code in c++, java & python"
print(cuteCat(matrix, string))