def dfs(idx, nums):
    if len(nums) == 3:
        result.append(nums[:])
        return
    for i in range(idx, len(cards)):
        dfs(i+1, nums+[cards[i]])
        
cards = [1, 2, 3, 4, 5]
result = []
dfs(0, [])
print(result)