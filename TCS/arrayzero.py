arr = list(map(int, input("Enter the numbers with space in between: ").split(" ")))
pos=0
for i in range(len(arr)):
    if arr[i]==0:
        continue
    else:
        if pos!=i:
            arr[pos],arr[i]=arr[i],arr[pos]
        pos+=1
print(arr)