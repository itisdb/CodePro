class linkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.check = False

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = list(map(int, input().split()))
    data = {}
    for i in range(n):
        data[pos[i]].append(linkedList(arr[i]).data)
    print(data)