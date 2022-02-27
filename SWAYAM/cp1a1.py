def cost(n:list):
    if len(n)>0:
        return max(n)-min(n)
    else:
        return 0

test = int(input())
output = []
for i in range(test):
    balls = int(input())
    n = list(map(int,input().split()))
    output.append(cost(n))

for i in output:
    print(i)

    