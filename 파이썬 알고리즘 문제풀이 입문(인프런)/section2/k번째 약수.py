import sys

for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/1. k번째 약수/in{}.txt".format(i), "rt")

    n, k = map(int, input().split())

    order = 0
    answer = -1
    for i in range(1, n+1):
        if n % i == 0:
            order += 1
        if order >= k:
            answer = i
            print(answer)
            break
    else:
        print(answer)