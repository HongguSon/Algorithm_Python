# 21608번

n = int(input())
favors = []
for i in range(n**2):
    students = list(map(int, input().split()))
    favors.append((students[0], students[1:]))

seat = [[0]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def count(r, c, favor):
    like = 0
    empty = 0
    for k in range(4):
        dr = r + dx[k]
        dc = c + dy[k]
        if 0 <= dr < n and 0 <= dc < n:
            if seat[r][c] == 0:
                if seat[dr][dc] == 0:
                    empty += 1
                elif seat[dr][dc] in favor[1]:
                    like += 1
    return like, empty


def likes(r, c, favor):
    like = 0
    for k in range(4):
        dr = r + dx[k]
        dc = c + dy[k]
        if 0 <= dr < n and 0 <= dc < n:
            if seat[dr][dc] in favor[1]:
                like += 1
    return like


final_decision = []
for favor in favors:
    # print(favor[0])
    my_seat = []
    for i in range(n):
        for j in range(n):
            like, empty = count(i, j, favor)
            my_seat.append([i, j, like, empty])
    my_seat.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    # print(my_seat)
    # print(favor[0])
    for my in my_seat:
        xx, yy = my[0], my[1]
        if seat[xx][yy] == 0:
            seat[xx][yy] = favor[0]
            break
    final_decision.append([favor, xx, yy])
    # print(xx, yy)
    # print(seat,'\n')
# print(seat)

answer = 0
for final in final_decision:
    like = likes(final[1], final[2], final[0])
    if like == 0:
        continue
    else:
        answer += 10**(like-1)
print(answer)
