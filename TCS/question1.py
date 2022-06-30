n = int(input("Enter the number of checkins: "))
ci=[]
co=[]

# input
ci = list(map(int, input("Enter checkin dates with spaces: ").split(" ")))
co = list(map(int, input("Enter checkout dates with spaces: ").split(' ')))

d = {}
for i in range(n):
	inp=ci[i]
	out=co[i]
	for j in range(inp,out):
		if j in d:
			d[j]+=1
		else:
			d[j]=1

d = dict(sorted(d.items(),key=lambda x:x[1]))
print("Max Customer Day: ",list(d.items())[-1][0])