class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr=sorted(arr, key=abs)
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            while dic[i] > 0:
                if 2 * i in dic and dic[2 * i] > 0:
                    dic[2 * i] -= 1
                else:
                    return False
                dic[i] -= 1    
        return True
