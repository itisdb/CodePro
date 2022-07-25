def selfSuf(N, money, books)->int:
	left = [books[i]-money[i] for i in range(N)]
	left = sorted(left)
	saved = 0
	toborrow = 0
	for i in range(N):
		if left[i]<0:
			saved+=abs(left[i])
		else:
			toborrow+=abs(left[i])
	return toborrow-saved
if __name__=='__main__':
	N = int(input("Enter the number of items: "))
	money = list(map(int,input("Enter the money array: ").split(' ')))
	books = list(map(int, input("Enter the books array: ").split(' ')))
	print(selfSuf(N, money, books))