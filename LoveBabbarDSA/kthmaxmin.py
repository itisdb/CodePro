arr = list(map(int,input("Enter arr: ").split(' ')))

arr = sorted(arr)

k = int(input("enter k: "))

print(arr[k-1])
print(arr[-k])