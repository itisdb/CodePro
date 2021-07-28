class Solution:
    def beautifulArray(self, n: int):
        if n==1:
            return [1]
        if n==2:
            return [1,2]
        res = [i for i in range(1,n)]
        j=2
        while j<n:
            i=0
            k=i+1
            while i<j-1:
                if res[k]*2==res[i]+res[j]:
                    if abs(i-k)>abs(j-k):
                        res[k],res[j]=res[j],res[k]
                    else:
                        res[k],res[i]=res[i],res[k]
                if k==j-1:
                    i+=1
                    k=i+1    
                else:
                    k+=1
            j+=1       
        return res
if __name__ == '__main__':
    solution = Solution()
    print(solution.beautifulArray(4))