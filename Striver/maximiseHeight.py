inp = (input("Enter the Array(comma separated):")).split(',')
inp = [int(i) for i in inp]
# for the input of the array
# print(inp)

k = int(input("Enter K: "))

inp=sorted(inp)
l=len(inp)-1
maxm=inp[l]
minm=inp[0]
height=maxm-minm
for i in range(1,l+1):
	minm=min(inp[0]+k, inp[i]-k)
	maxm=max(inp[l]-k, inp[i-1]+k)
	height=min(height,maxm-minm)
print("Maximum Difference is "+str(height))

