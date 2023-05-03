# 21610번
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move_list = [(list(map(int,input().split()))) for _ in range(m)]

clouds = deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])

movement = [[0, -1], [-1, -1], [-1, 0], [-1, 1],
            [0, 1], [1, 1], [1, 0], [1, -1]]


def moving(clouds, move):
    d, s = move
    visited = [[False]*n for _ in range(n)]
    for cloud in clouds:
        cloud[0] = (cloud[0] + movement[d-1][0] * s) % n
        cloud[1] = (cloud[1] + movement[d-1][1] * s) % n
        board[cloud[0]][cloud[1]] += 1
        visited[cloud[0]][cloud[1]] = True

    for cloud in clouds:
        for i in range(1, 8, 2):
            x, y = cloud[0], cloud[1]
            nx = x + movement[i][0]
            ny = y + movement[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] > 0:
                    board[x][y] += 1

    new_clouds=[]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if board[i][j] >= 2:
                    new_clouds.append([i, j])
                    board[i][j] -= 2

    return new_clouds


for i in range(len(move_list)):
    clouds = moving(clouds, move_list[i])

answer = 0
for i in range(n):
    answer += sum(board[i])
print(answer)
