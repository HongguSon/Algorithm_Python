# 20055번
from collections import deque

n, k = map(int, input().split())
belt = deque(map(int, input().split()))

robots = []

flag = 0
while True:
    flag += 1
    belt.rotate()
    if len(robots) > 0:
        robots = [i+1 for i in robots]
        if robots[0] >= n-1:
            del robots[0]
    if robots:
        # print(robots)
        for i, robot in enumerate(robots[:]):
            if belt[robot+1] > 0 and robot+1 not in robots:
                if robot+1 < n-1:
                    belt[robot + 1] -= 1
                    # print(robots, i)
                    robots[robots.index(robot)] += 1
                else:
                    # print(i, robots)
                    del robots[i]
                    belt[robot + 1] -= 1
    # print(belt)
    if belt[0] > 0:
        robots.append(0)
        belt[0] -= 1
    # print(belt)
    # print(robots)
    if belt.count(0) >= k:
        break
print(flag)


