class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if str[0]=='0':
            return 0
        res=[]
        pos=0
        lastindex=0
        while pos<len(num)-1:
            if num[pos]>num[pos+1] and num[pos+1]!='0':
                res.append(str[lastindex:pos+1])
                lastindex=pos+1
            if num[pos+1]