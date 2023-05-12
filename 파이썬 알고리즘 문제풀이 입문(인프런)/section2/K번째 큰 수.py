import sys

def dfs(idx, nums):
    if len(nums) == 3:
        result.append(sum(nums[:]))
        return
    for i in range(idx, n):
        dfs(i+1, nums+[cards[i]])
    
    
    
for i in range(1, 6):
    sys.stdin = open("./pythonalgorithm_formac/섹션 2/3. k번째 큰 수/in{}.txt".format(i), "rt")
    n, k = map(int, input().split())
    cards = list(map(int, input().split()))
    result = []
    dfs(0, [])
    result = list(set(result))
    print(sorted(result, reverse=True)[k-1])
    
# 강의 풀이 (3중 for문)
# for i in range(1, 6):
#     sys.stdin = open("./pythonalgorithm_formac/섹션 2/3. k번째 큰 수/in{}.txt".format(i), "rt")
#     n, k = map(int, input().split())
#     cards = list(map(int, input().split()))
#     res = set()
#     for x in range(n):
#         for y in range(y+1, n):
#             for z in range(z+1, n):
#                  res.add(cards[x] + cards[y] + cards[z])
#     res = list(res)
#     res.sort(reverse=True)
#     print(res[k-1])
    
    

    
    
                
    