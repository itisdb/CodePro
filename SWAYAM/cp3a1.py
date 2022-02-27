test = int(input())


for i in range(test):
    N, X = list(map(int, input().split()[:2]))
    time = {}
    people = 'a'
    for i in range(N):
        time[people]=(list(map(int, input().split()[:2])))
        people = chr(ord(people)+1)
    print(time)