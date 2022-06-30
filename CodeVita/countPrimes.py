def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
             
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    count = 0
    for p in range(n + 1):
        if prime[p]:
            count+=1
    return count

num = int(input())
c=0
while num>1:
    num = num - SieveOfEratosthenes(num)
    c+=1

c+=1
print(c,end='')