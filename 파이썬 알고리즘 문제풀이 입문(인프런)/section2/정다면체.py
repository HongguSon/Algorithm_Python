import sys
    
for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/5. 정다면체/in{}.txt".format(i), "rt")
    n, m = map(int, input().split())
    answer = [i for i in range(n+1, m+2)]
    print(*answer)
    
    
    