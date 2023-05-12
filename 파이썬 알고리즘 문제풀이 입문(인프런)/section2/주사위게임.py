import sys
    
def count_prize(x):
    how_many = len(set(x))
    if how_many == 1:
        return (x[0]*1000) + 10000
    elif how_many == 2:
        return (sorted(x)[1]*100) + 1000
    else:
        return max(x)*100
        
    
for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/9. 주사위 게임/in{}.txt".format(i), "rt")
    n = int(input())
    answer = -1
    for _ in range(n):
        dices = list(map(int, input().split()))
        answer = max(answer, count_prize(dices))
    print(answer)