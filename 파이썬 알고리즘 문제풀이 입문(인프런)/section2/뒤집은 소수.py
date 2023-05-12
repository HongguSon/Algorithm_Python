import sys
    
def reverse(x):
    return int(x[::-1])

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    else:
        return True
    
for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/8. 뒤집은 소수/in{}.txt".format(i), "rt")
    n = int(input())
    nums = list(map(reverse, input().split()))
    for num in nums:
        if isPrime(num):
            print(num, end=' ')
    print()