# 17140번
from collections import Counter

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
rowA, colA = 3, 3


def calc(list):
    list = [item for item in list if item != 0]
    result = Counter(list).most_common()
    result.sort(key=lambda x: (x[1], x[0]))
    output = [x for y in result for x in y]
    if len(result) > 100:
        return result[:100]
    else:
        return output


def transpose(A):
    At = [[False]*rowA for _ in range(colA)]
    for i in range(rowA):
        for j in range(colA):
            At[j][i] = A[i][j]
    return At, colA, rowA


def R(A):
    global rowA, colA
    for i, row in enumerate(A):
        A[i] = calc(row)
    colA = len(max(A, key=len))
    for i, row in enumerate(A):
        if len(row) < colA:
            A[i] = row + [0]*(colA-len(row))
    return A

def C(A):
    global rowA, colA
    A, rowA, colA = transpose(A)
    for i, row in enumerate(A):
        A[i] = calc(row)
    colA = len(max(A, key=len))
    for i, row in enumerate(A):
        if len(row) < colA:
            A[i] = row + [0]*(colA-len(row))
    A, rowA, colA = transpose(A)
    return A

cnt = 0
while True:
    if rowA>=r and colA>=c and A[r-1][c-1] == k:
        print(cnt)
        break
    else:
        if rowA >= colA:
            A = R(A)
        else:
            A = C(A)
        cnt += 1
    if cnt > 100:
        print(-1)
        break