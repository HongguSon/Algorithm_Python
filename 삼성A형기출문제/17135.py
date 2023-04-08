# 17135번

from copy import deepcopy

n, m, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
archers = [i for i in range(m)]
combinations = []  # 궁수 배치 조합


def dfs(idx, array, r):
    if len(array) == r:
        combinations.append(array[:])
        return
    for i in range(idx, m):
        dfs(i + 1, array + [archers[i]], 3)


dfs(0, [], 3)

result = 0

# 적이 있는 좌표를 저장
original_enemy = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            original_enemy.append((i, j))


def calc(r1, c1, c2):
    return abs(r1 - n) + abs(c1 - c2)


for archer in combinations:

    enemy = deepcopy(original_enemy)[::-1]
    kill = 0

    for k in range(n):
        # 밑으로 한 칸 내려와 없어 지는 적 처리
        for x in deepcopy(enemy):
            if x[0] + k >= n:
                enemy.remove(x)
        if len(enemy) == 0:
            break
        else:
            target = [False, False, False]
            for j in range(3):
                for i in enemy:
                    #적이 한 칸 내려오게 되면 어차피 거리는 기존보다 1만큼 줄어들기 때문에, 아래와 같은 로직 사용
                    if calc(i[0], i[1], archer[j]) - k <= d:
                        if not target[j]:
                            target[j] = i
                        #반드시 왼쪽에 있는 최단 경로가 선택되어야함
                        elif calc(target[j][0], target[j][1], archer[j]) > calc(i[0], i[1], archer[j]):
                            target[j] = i
                        elif calc(target[j][0], target[j][1], archer[j]) == calc(i[0], i[1], archer[j]):
                            if i[1] < target[j][1]:
                                target[j]=i
            for i in set(target):
                if type(i) is tuple:
                    kill += 1
                    enemy.remove(i)
    if kill > result:
        result = kill
        kill = 0
print(result)