nums = list(map(int, input("Enter the numbers with space:").split(" ")))
start = nums[0]
end = nums[1]

# Check for the number being a positive integer.
if start<0 or end<0:
	print("-1")

def rep(num):
	num=str(num)
	for i in range(len(num)):
		if num[i] in num[i+1:]:
			return True
	return False

count=0
for j in range(start, end+1):
	if not rep(j):
		count+=1

print("Count: ",count)
