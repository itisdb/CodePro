def mypair(k,arr):
    count=0
    for i in arr:
        if (i+k) in arr:
            count+=1
    return count
    

print(mypair(2, [1,5,3,4,2]))