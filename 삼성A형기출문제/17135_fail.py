#17135번

import sys
from collections import deque
input = sys.stdin.readline

n, m, d = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(n) ]
archers = [ i for i in range(m) ]
combinations = [] #궁수 배치 조합

def dfs(idx, list, r):
    global m
    if len(list) == r:
        combinations.append(list[:])
        return
    for i in range(idx, m):
        dfs(i+1, list+[archers[i]], 3)
dfs(0, [], 3)

result = -sys.maxsize

for archer in combinations:
    kill = 0
    for i in range(n-1, -1, -1):
        enemy = [False, False, False]
        for j in range(m):
            if grid[i][j] == 1:
                for k in range(3):
                    archer_distance = (n-i)+abs(archer[k]-j)
                    if d >= archer_distance:
                        if not enemy[k]:
                            enemy[k]=(j, archer_distance)
                        elif enemy[k][1] > archer_distance:
                            enemy[k]=(j, archer_distance)
        print(archer,'일 때',enemy)
        coordinate = []
        for l in range(3):
            if enemy[l]:
                coordinate.append(enemy[l][0])
        kill += len(set(coordinate))
    if kill > result:
        result = kill
print(result)
            

        