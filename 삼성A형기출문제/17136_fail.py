#17136번
#실패. 그리디 알고리즘으로 풀려고 했지만 예외처리가 너무 말이 안됨.
from itertools import permutations

matrix = [ list(map(int, input().split())) for _ in range(10) ]
need = []

for i in range(10):
    for j in range(10):
        if matrix[i][j] == 1:
            need.append((i,j))

def square(i,j,need):
    flag = False
    length = 1
    while True: 
        for r in range(length+1):
            for c in range(length+1):
                if (i+r,j+c) in need:
                    continue
                else:
                    flag = True
                    break
            if flag: break
        else:
            length += 1
            if length == 5:
                flag: True
                break
        if flag: break
    return length

use = [0, 0, 0, 0, 0]
x = 0

max_length = dict()
for coord in need:
    each_length = square(coord[0], coord[1], need)
    if each_length != 1:
        max_length[coord] = each_length

order = [[] for _ in range(4)]
for k, v in max_length.items():
    order[v-1].append((k,v))
        
final_order = []
for i in range(3,-1,-1):
    if order[i]:
        if len(order[i]) == 1:
            X, Y = order[i][0][0], order[i][0][1]
            for r in range(order[i][1]):
                for c in range(order[i][1]):
                    need.remove((X+r, Y+c))
            use[order[i][1]-1] += 1
            if use[order[i][1]-1] > 5:
                print(-1)
                break
        else:
            for paper_order in permutations(order[i]):
                flag2 = False
                for paper in paper_order:
                    X, Y = order[i][0][0], order[i][0][1]
                    for r in range(order[i][1]):
                        for c in range(order[i][1]):
                            if (X+r, Y+c) not in need:
                                flag2 = True
                                break
                        if flag2: break
                    else:
                        for r in range(order[i][1]):
                            for c in range(order[i][1]):
                                need.remove((X+r, Y+c))
                        use[order[i][1]-1] += 1
                        if use[order[i][1]-1] > 5:
                            print(-1)
                            break
else:
    print(sum(use))
# 가장 큰 길이부터 순열로 묶어서 집어넣고, 그 중 가장 많은 개수를 찾는다.

# while 
#     X, Y = need[x][0], need[x][1]
#     for i in range(length):
#         for j in range(length):
#             need.remove((X+i, Y+j))
#     use[length-1] += 1
#     if use[length-1] > 5:
#         print(-1)
#         break
# else:
#     print(sum(use))

'''0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0'''
                        