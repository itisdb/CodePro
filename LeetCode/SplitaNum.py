class Solution:
    def numberOfCombinations(self, num: str) -> int:
        def seprateNumbers():
            if str[0]=='0':
                return 0
            sub=""
            isValid=False
            for i in range(1,(len(num)//2)+1):
                sub=num[0:i]
                n=int(sub)
                validString=sub
                while(len(validString)<len(num)):
                    n+=1
                    validString+=str(n)
                if num==validString:
                    isValid=True
                    break

                
                    
            