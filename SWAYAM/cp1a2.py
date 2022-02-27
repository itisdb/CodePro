def GCD(s,n):
    temp=s//n
    while True:
        if s%temp==0:
            print(temp)
            break
        else:
            temp-=1

N,M = input().split(' ')
GCD(int(M),int(N))

