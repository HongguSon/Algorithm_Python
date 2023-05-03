#14987번
from collections import deque

gears = [ deque(map(int,input())) for _ in range(4) ]
k = int(input())
rotates = [ list(map(int, input().split())) for _ in range(k)]

def rotation(n, d, gears):
    rotate_list = [False, False, False, False]
    rotate_list[n-1] = d
    
    def rotate_right(n,d):
        if n >= 4:
            return
        if gears[n-1][2] != gears[n][6]:
            rotate_list[n] = -d
            rotate_right(n+1, -d)
        else: return
        
    def rotate_left(n,d):
        if n <= 1:
            return
        if gears[n-1][6] != gears[n-2][2]:
            rotate_list[n-2] = -d
            rotate_left(n-1, -d)
        else: return
        

    if 1 <= n <= 3:
        rotate_right(n, d)
    if 2 <= n <= 4:
        rotate_left(n, d)
    return rotate_list
    
for rotate in rotates:
    result = rotation(rotate[0], rotate[1], gears)
    for i, x in enumerate(result):
        if x:
            gears[i].rotate(x)
# print(gears)

answer = 0
for i, gear in enumerate(gears):
    answer += ((2**i)*gear[0])
print(answer)