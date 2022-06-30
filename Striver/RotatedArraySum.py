def rotatedArray (l,target):
	index = 0
	for i in range(len(l)-1):
		if l[i]>l[i+1]:
			index = i+1
			break
	l=l[index:]+l[0:index]
	res=[]
	beg = 0
	end = len(l)-1
	while (l[beg]+l[end])>target:
		end-=1
	if l[beg]+l[end]==target:
		while(beg<end):
			res.append([l[beg],l[end]])
			beg+=1
			end-=1
	print(res)


rotatedArray([i for i in range(1,23)],17)

