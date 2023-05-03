# 15686번

n, m = map(int, input().split())
city = [ list(map(int,input().split())) for _ in range(n) ]
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))
home = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i,j))

#dfs로 조합 짜기
combination = []
def dfs(idx, list):
    if m == len(list):
        combination.append(list[:])
        return
    for i in range(idx, len(chicken)):
        dfs(i+1, list+[chicken[i]])
dfs(0,[])

def calc(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)

answer = float('inf')
# answer = []
for choices in combination:
    result = 0
    for house in home:
        distance = float('inf')
        for choice in choices:
            distance = min(distance, calc(choice[0],choice[1],house[0],house[1]))
        result += distance
    answer = min(answer, result)
    # answer.append(result)
print(answer)
            