from itertools import permutations
def countArrangement(n):
    list = []
    flag=False
    count=0
    for i in range(1, n):
        list.append(i)
    perm=permutations(str(list))
    for i in perm:
        j=0
        while(j<len(perm[i])):
            if(int(perm[i][j])%j)==0 or (j%int(perm[i][j]))==0:
                continue
            else:
                flag=True
                break
            j=j+1
        if flag==False:
            count=count+1
        else:
            flag=False
    return count
        
        
        
if __name__ == '__main__':
     n=int(input())
     print(countArrangement(n))