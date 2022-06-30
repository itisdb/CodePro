t=int(input())
for k in range(t):
    n=int(input())
    l1 = list(map(int,input().split()))[:n]
    j=0
    c=0
    for i in sorted(l1):
        if i>j:
            c+=1
            j+=1
    print('Case #'+str(k+1)+':',c)