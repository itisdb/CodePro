def sort012(arr,n):
    count0,count1,count2 = 0,0,0
    for i in range(n):
        if arr[i]==0:
            count0+=1
        elif arr[i]==1:
            count1+=1
        elif arr[i]==2:
            count2+=1
    for i in range(n):
        if i<count0:
            arr[i] = 0
        elif i<count0+count1:
            arr[i] = 1
        elif i<count0+count1+count2:
            arr[i] = 2
    return arr

if __name__ == '__main__':
    N = int(input("N = "))
    arr = list(map(int, input("arr[] = ").split(' ')))
    print(sort012(arr=arr, n=N))