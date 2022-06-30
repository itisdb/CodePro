# Snake And Ladder
n = 10

board = []
for i in range(n):
    if i % 2 == 1: board = input().split() + board
    else: board = input().split()[::-1] + board
board = ['0'] + board

memo = ['0'] * 101
cp = {'Start': 1, 'End': 100}

for i, t in enumerate(board):
    if (t[0] == 'S' or t[0] == 'L') and t[1] == '(':
        if t[2].isdigit():
            memo[i] = int(t[2:-1])
        else: memo[i] = cp[t[2:-1]]
    else:
        memo[i] = cp.get(t[2:-1], i)

dice = list(map(int, input().split()))
curr = 0
s, l = 0, 0

for t in dice:
    if curr + t < 101: curr += t
    while memo[curr] != curr: 
        if curr > memo[curr]: s += 1
        else: l += 1
        curr = memo[curr]

if curr == 100:
    print(f'Possible {s} {l}')
else: 
    print(f'Not possible {s} {l} {"Start" if curr == 1 else curr}')