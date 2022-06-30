def saveThePrisoner(n,m,s):
    for i in range(m):
        if s>n:
            s=1
            continue
        s=s+1
    print(s-1)
    
saveThePrisoner(5, 2, 2)