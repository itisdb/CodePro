from itertools import permutations
def smallestNumber(num: int) -> int:
    if num == 0:
        return 0
    def greatestCombo(n: int):
        n=(str(n))[1:]
        arr = "".join(sorted((n),reverse=True))
        return arr
    def smallestCombo(n: int):
        nstr=str(n)
        arr = (sorted((nstr),reverse=False))
        # print(arr[0])
        #checking for the first non zero value
        i=0
        if arr[0]=='0':
            while(arr[i]=='0'):
                i+=1
            temp = arr[0]
            arr[0] = arr[i]
            arr[i] = temp
            
        res=(''.join(arr))
        return res
    if num < 0:
        return int('-'+str(greatestCombo(num)))
    else:
        return int(smallestCombo(num))


