# 14500번

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = -float('inf')
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(cnt, start, sigma):
    global answer
    if cnt == 4:
        answer = max(sigma, answer)
        return
    r, c = start
    for i in range(4):
        nr = r+move[i][0]
        nc = c+move[i][1]
        if 0 <= r+move[i][0] < n and 0 <= c+move[i][1] < m:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(cnt+1, (nr, nc), sigma + board[nr][nc])
                visited[nr][nc] = False


comb = [False]*4
comb_result = []


def combination(idx, list):
    if len(list) == 3:
        comb_result.append(list[:])
        return
    for i in range(idx, 4):
        list.append(move[i])
        combination(i+1, list)
        list.pop()


combination(0, [])


def special(start):
    global answer
    x, y = start
    for direction in comb_result:
        flag = 1
        for d in direction:
            if 0 <= x + d[0] < n and 0 <= y + d[1] < m:
                continue
            else:
                flag = 0
        if flag:
            result = board[x][y]
            for d in direction:
                result += board[x+d[0]][y+d[1]]
            answer = max(result, answer)


visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        special((i, j))
        visited[i][j] = True
        dfs(1, (i, j), board[i][j])
        visited[i][j] = False

print(answer)
