def findElements(a, n):
    s = list(set(a))
    s = sorted(s, reverse=True)
    for i in range(n):
        if a[i]!=s[0] and a[i]!=s[1]:
            print(a[i], end=" ")  

a = list(map(int, input().split(" ")))
n = len(a)
findElements(a, n)