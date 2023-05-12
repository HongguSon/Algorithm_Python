import sys
    
for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/7. 소수(에라토스테네스 체)/in{}.txt".format(i), "rt")
    n = int(input())
    prime = [False, False] + [True]*(n-1)
    answer = []
    for i in range(2, n):
        if prime[i]:
            answer.append(i)
            for j in range(2*i, n+1, i):
                prime[j] = False
    print(len(answer))