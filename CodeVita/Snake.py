gameboard = []
for i in range(10):
    if i % 2 == 1:
        gameboard = input().split() + gameboard
    else:
        gameboard = input().split()[::-1] + gameboard
gameboard = ['0'] + gameboard

gameNum = ['0'] * 101
denote = {'Start': 1, 'End': 100}

for i, t in enumerate(gameboard):
    if (t[0] == 'S' or t[0] == 'L') and t[1] == '(':
        if t[2].isdigit():
            gameNum[i] = int(t[2:-1])
        else:
            gameNum[i] = denote[t[2:-1]]
    else:
        gameNum[i] = denote.get(t[2:-1], i)

dice = list(map(int, input().split()))
curr = 0
snake, ladder = 0, 0

for t in dice:
    if curr + t < 101:
        curr += t
    while gameNum[curr] != curr: 
        if curr > gameNum[curr]:
            snake += 1
        else:
            ladder += 1
        curr = gameNum[curr]

if curr == 100:
    print('Possible',end=' ')
    print(snake,end=' ')
    print(ladder,end=' ')
else: 
    print('Not possible',end=' ')
    print(snake,end=' ')
    print(ladder,end=' ')
    print("Start" if curr == 1 else curr)