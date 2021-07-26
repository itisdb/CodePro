class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res=[]
        def dfs(num,path):
            if not num:
                res.append(path)
                return
            for i in d[num[0]]:
                dfs(num[1:],path+i)
        dfs(digits,'')
        return res
        