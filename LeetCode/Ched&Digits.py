import math

tc= int(input())
c=[]
while(tc>0):
    n= int(input())
    count=0
    for i in range(n+1):
        if '0' not in str(i):
            fac= math.factorial(len(str(i)))
            product=1
            for j in str(i):
                product *= int(j)
                
            if product>= fac:
                count+=1
                
    c.append(count)
    tc-=1

for i in c:
    print(i)