def maxDiff(a, n) -> int: 
    # O(n**2) approach below
    # max_diff = 0
    # for i in range(n):
    #     for j in range(i, n):
    #         if a[i]<a[j]:
    #             max_diff = max(max_diff,j-i)
    # return max_diff

    # trying for the O(n) approach
    max_diff = 0
    i=0
    j=0
    while i<n and j<n:
        if a[i]<=a[j]:
            j+=1
        elif a[j]<a[i]:
            i+=1
            j=i+1



if __name__ == '__main__':
    inputs = int(input("Enter the number of values: "))
    testcases = []
    sizes = []
    for i in range(inputs):
        sizes.append(int(input("Enter the size: ")))
        testcases.append(list(map(int, input("Enter the {} integers: ".format(sizes[i])).split(' '))))

    for i in range(len(sizes)):
        print(maxDiff(a=testcases[i],n=sizes[i]),end=" ")
    print()