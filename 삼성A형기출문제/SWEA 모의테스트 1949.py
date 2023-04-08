# 1949번 등산로 조성
import sys
sys.stdin = open("input.txt", "r")

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(start, cnt, board):
    global max_value
    x, y = start
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] < board[x][y]:
                dfs((nx, ny), cnt+1, board)
    else:
        max_value = max(max_value, cnt)
        return


T = int(input())
for test_case in range(1, T + 1):
    max_value = -int(2e9)
    N, K = map(int, input().split())
    board = []
    highest = 0
    high_coord = []
    for n in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        highest = max(sorted(row)[-1], highest)
    for r in range(N):
        for c in range(N):
            if board[r][c] == highest:
                high_coord.append((r, c))

    for coord in high_coord:
        for k in range(K+1):
            if k == 0:
                dfs(coord, 1, board)
            else:
                for i in range(N):
                    for j in range(N):
                        temp = [item[:] for item in board]
                        temp[i][j] -= k
                        dfs(coord, 1, temp)
    print('#{} {}'.format(test_case, max_value))


