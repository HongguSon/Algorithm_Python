import sys
    
def digit_sum(x):
    return sum(list(map(int, list(str(x)))))
    
for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/6. 자릿수의 합/in{}.txt".format(i), "rt")
    n = int(input())
    nums = list(map(int, input().split()))
    answer_idx = False
    max_num = -1
    for idx, num in enumerate(nums):
        if max_num < digit_sum(num):
            max_num = digit_sum(num)
            answer_idx = idx
    print(nums[answer_idx])