arr = list(map(int, input("Enter the array: ").split(" ")))
left=[]
right=[]
for i in range(len(arr)):
	if (arr[i]%10==0):
		right.append(arr[i])
	else:
		left.append(arr[i])

ans=left+right
print(ans)