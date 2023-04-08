# 16234.py
from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def make_party(node: tuple):
    q = deque()
    q.append(node)

    graph = [node]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if L <= abs(A[nx][ny]-A[x][y]) <= R:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    graph.append((nx, ny))
    return graph


result = 0
while True:
    visited = [[False] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                party = make_party((i, j))
                if len(party) > 1:
                    flag = 1
                    mean = sum([A[x][y] for x, y in party]) // len(party)
                    for x, y in party:
                        A[x][y] = mean
    if flag == 0:
        break
    result += 1
print(result)
