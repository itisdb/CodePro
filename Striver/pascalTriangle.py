def pascal(n):
    space = n-1
    for i in range(n):
        print(' '*space,end="")
        out = str(pow(11,i))
        for _ in out:
            print(_+" ",end="")
        space-=1
        print()

n = int(input())
pascal(n)