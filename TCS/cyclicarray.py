arr = input("Enter the Array: ")
arr = [int(i) for i in arr.split(" ")]

k=(int)(input("Enter the K: "))
rev=[]
r=k

for i in arr[::-1]:
	if k>0:
		rev.append(i)
		k-=1

ans = [arr[0]]
ans.extend(rev)
ans.extend(arr[1:(len(arr)-r)])
print(ans)