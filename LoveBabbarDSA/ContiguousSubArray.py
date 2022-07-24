def maxSubArray(arr,N):
    pass

if __name__ == '__main__':
    N = int(input("N = "))
    arr = list(map(int,input("Arr[] = ").split(' ')))
    print(maxSubArray(arr=arr, N=N))