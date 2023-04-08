# 15686번

n = int(input())
dragon_info = [list(map(int, input().split())) for _ in range(n)]


def direction(x, y, d):
    if d == 0:
        return x+1, y
    elif d == 1:
        return x, y-1
    elif d == 2:
        return x-1, y
    elif d == 3:
        return x, y+1

def make_growth(body: list):
    ex, ey = body[-1]
    for i in range(len(body)-2, -1, -1):
        x, y = body[i]
        if x - ex > 0 and y - ey > 0: # 1사분면
            body.append((ex - y + ey, ey + x - ex))
        elif x - ex < 0 and y - ey > 0: # 2사분면
            body.append((ex - y + ey, ey - ex + x))
        elif x - ex < 0 and y - ey < 0: # 3사분면
            body.append((ex + ey - y, ey - ex + x))
        elif x - ex > 0 and y - ey < 0:
            body.append((ex + ey - y, ey + x - ex))
        elif ey == y:
            body.append((ex, ey-ex+x))
        elif ex == x:
            body.append((ex+ey-y, ey))

    return body


def generation(dragon: list):
    body = []
    x, y, d, g = dragon
    body.append((x, y))  # 시작 점
    x1, y1 = direction(x, y, d)
    body.append((x1, y1)) # 0세대
    for i in range(g):
        body = make_growth(body)
    # print('이번 드래곤은', body)
    return body

final = []
for dragon in dragon_info:
    body = generation(dragon)
    final.extend(body)
final = sorted(list(set(final)))

cnt = 0
for idx, coord in enumerate(final):
    x0, y0 = coord
    if idx >= len(final)-1:
        continue
    if final[idx+1] == (x0, y0 + 1):
        if (x0+1, y0) in final and (x0+1, y0+1) in final:
            cnt += 1
print(cnt)





