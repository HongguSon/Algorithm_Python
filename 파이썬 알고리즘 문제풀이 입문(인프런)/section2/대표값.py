import sys
    
for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/4. 대표값/in{}.txt".format(i), "rt")
    n = int(input())
    students = list(map(int, input().split()))
    mean = round(sum(students)/n)
    difference = [abs(x-mean) for x in students]
    nearest = min(difference)
    print(mean, difference.index(nearest)+1)
    