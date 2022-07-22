def maxDiff(a, n) -> int: 
    # O(n**2) approach below
    # max_diff = 0
    # for i in range(n):
    #     for j in range(i, n):
    #         if a[i]<a[j]:
    #             max_diff = max(max_diff,j-i)
    # return max_diff

    max_diff = 0
    start = 0
    end = 0
    for i in range(n):
        if a[start]>a[i]:
            end=i
            max_diff = max(max_diff, end-start) 
            start = i
    return max_diff



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