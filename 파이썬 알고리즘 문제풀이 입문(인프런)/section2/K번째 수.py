import sys

for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/2. K번째 수/in{}.txt".format(i), "rt")
    T = int(input())
    for _ in range(T):
        n, s, e, k = map(int, input().split())
        nums = list(map(int, input().split()))
        print('#{} {}'.format(_+1, sorted(nums[s-1:e])[k-1]))