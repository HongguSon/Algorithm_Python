import sys

for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/10. 점수 계산/in{}.txt".format(i), "rt")
    n = int(input())
    score = list(map(int, input().split()))
    flag = 0
    answer = 0
    for i in range(n):
        if score[i] == 1:
            answer += flag + 1
            flag += 1
        else:
            flag = 0
    print(answer)