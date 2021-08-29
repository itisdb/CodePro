def MergeSort(A):
    if len(A)>1:
        mid=len(A)//2
        left=A[:mid]
        right=A[mid:]
        MergeSort(left)
        MergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                A[k]=left[i]
                i+=1
            else:
                A[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            A[k]=left[i]
            i+=1
            k+=1

        while i<len(right):
            A[k]=right[i]
            i+=1
            k+=1

