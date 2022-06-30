arr = list(map(int, input("Enter the array: ").split(' ')))

k = (int)(input("Enter the K: "))
left=[]
for i in range(k):
	left.append(arr[i])

ans=arr[k:]+left
print(ans)