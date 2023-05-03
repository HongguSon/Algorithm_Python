# 3190번
from collections import deque

n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for i in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
l = int(input())
move = [list(input().split()) for _ in range(l)][::-1]

time = 0
snake = deque()
snake.append([0, 0])
d = 1
next_moving = move.pop()
while True:
    if time == int(next_moving[0]):
        if next_moving[1] == 'D':
            d = (d+1) % 4
        else:
            d = (d+3) % 4
        if len(move) > 0:
            next_moving = move.pop()

    x, y = snake[-1][0], snake[-1][1]
    if d == 0:
        if x-1 < 0 or [x-1, y] in snake:
            break
        else:
            snake.append([x-1, y])
            if board[x - 1][y] != 1:
                snake.popleft()
            else:
                board[x-1][y] = 0
    elif d == 1:
        if y+1 >= n or [x, y+1] in snake:
            break
        else:
            snake.append([x, y+1])
            if board[x][y+1] != 1:
                snake.popleft()
            else:
                board[x][y+1] = 0
    elif d == 2:
        if x+1 >= n or [x+1, y] in snake:
            break
        else:
            snake.append([x+1, y])
            if board[x+1][y] != 1:
                snake.popleft()
            else:
                board[x+1][y] = 0
    elif d == 3:
        if y-1 < 0 or [x, y-1] in snake:
            break
        else:
            snake.append([x, y-1])
            if board[x][y-1] != 1:
                snake.popleft()
            else:
                board[x][y-1] = 0
    time += 1
print(time+1)


