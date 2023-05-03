# 동전 챙기기

from collections import deque

n = int(input())
board = []
check = [str(i) for i in range(1, 10)]
coin = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    row = list(input())
    board.append(row)
    for j in range(n):
        if row[j] in check:
            coin.append([int(row[j]), i, j])
        elif row[j] == 'S':
            start = (i, j)
        elif row[j] == 'E':
            end = (i, j)
coin.sort(key=lambda x: x[0])

result = []


def dfs(idx, list):
    if len(list) == 3:
        result.append(list[:])
        return
    for i in range(idx, len(coin)):
        dfs(i+1, list+[coin[i]])


dfs(0, [])


def bfs(start, end):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    while q:
        node = q.popleft()
        x, y, cnt = node
        if (x, y) == (end[0], end[1]):
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != '#':
                if not visited[nx][ny]:
                    q.append((nx, ny, cnt+1))
                    visited[nx][ny] = True
    return -1

min_value = int(2e9)
flag = 0
for coin_select in result:
    x1 = tuple(coin_select[0][1:])
    x2 = tuple(coin_select[1][1:])
    x3 = tuple(coin_select[2][1:])
    final = [start, x1, x2, x3, end]
    answer = 0
    for i in range(4):
        distance = bfs(final[i], final[i+1])
        if distance == -1:
            break
        else:
            answer += distance
    else:
        min_value = min(min_value, answer)

if min_value == int(2e9):
    print(-1)
else:
    print(min_value)