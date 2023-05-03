# 14499번

n, m, x, y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0] # 전개도 상 순서대로

for move in map(int, input().split()):
    # print('현재 좌표는', x, y)
    move -= 1
    if 0 <= x+dx[move] < n and 0 <= y+dy[move] < m:
        x += dx[move]
        y += dy[move]
        # print('움직임',x, y, move, dice)

        if move == 0:
            dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        elif move == 1:
            dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        elif move == 2:
            dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        elif move == 3:
            dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

        if board[x][y] == 0:
            board[x][y] = dice[-1]
        else:
            dice[-1] = board[x][y]
            board[x][y] = 0

        print(dice[0])
