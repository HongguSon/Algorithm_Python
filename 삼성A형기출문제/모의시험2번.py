# 신기한 Bucket
from collections import deque

n = int(input())
block_info = [list(map(int, input().split())) for _ in range(8)]
block_drop = [list(map(int, input().split())) for _ in range(n)]

info = deque([[0, 0, 0, 0] for _ in range(100)])

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def drop(k, c):
    if c > 0:
        i = 0
        while True:
            if info[i][c-1] == 0:
                info[i][c-1] = k
                break
            i += 1


def score(info):
    global result
    for i in range(100):
        if info[i].count(0) == 0:
            result += 1
            info.pop(i)
            info.append([0, 0, 0, 0])


def move(k, x, y):
    move_result = []
    for i in block_info[k-1]:
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and 0 <= ny < 4:
            move_result.append((k, nx, ny))
    return move_result

