t= int(input())
for j in range(1,t+1):
    s1 = list(map(int,input().split()))
    s2 = list(map(int,input().split()))
    s3 = list(map(int,input().split()))
    x= min(s1[0],s2[0],s3[0])
    y= min(s1[1],s2[1],s3[1])
    z= min(s1[2],s2[2],s3[2])
    w= min(s1[3],s2[3],s3[3])
    res = x+y+z+w
    if res==1000000:
        print('Case #'+str(j)+':',x,y,z,w)
    elif res<1000000:
        print('Case #'+str(j)+': IMPOSSIBLE')
    else:
        res=0
        i=0
        l1=[x,y,z,w]
        while res<1000000:
            res = res + l1[i]
            i+=1
            if res==1000000:
                l2=l1[:i]
            else:
                l2= l1[:i-1]
                l2.append(1000000-sum(l1[:i-1]))
            l2.extend(list(map(int,list('0'*(4-len(l2))))))
        print('Case #'+str(j)+':',*l2)