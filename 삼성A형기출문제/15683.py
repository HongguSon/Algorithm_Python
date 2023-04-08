# 15683번

from copy import deepcopy
n, m = map(int, input().split())
cctv = []
board = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [1, 2, 3], [0, 1, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
    ]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if 1 <= data[j] <= 5:
            cctv.append([data[j], i, j])


def fill(board, mode, x, y):
    for i in mode:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = -1


def dfs(depth, board):
    global min_value
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += board[i].count(0)
        min_value = min(min_value, cnt)
        return
    temp = deepcopy(board)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = deepcopy(board)


min_value = float('inf')
dfs(0, board)
print(min_value)