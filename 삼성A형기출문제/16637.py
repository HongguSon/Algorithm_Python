#16637번

from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
data = ''.join(input().split())

def calc(a, b, op):
    if op == '+':
        return int(a)+int(b)
    elif op == '-':
        return int(a)-int(b)
    else:
        return int(a)*int(b)
    
result = -sys.maxsize
temp = 0
def dfs(idx, prev):
    global result
    if idx >= n:
        result = max(result, prev)
        return
    if idx < n-3:
        dfs(idx+4, calc(prev, calc(data[idx+1],data[idx+3],data[idx+2]), data[idx]))
    dfs(idx+2, calc(prev, data[idx+1], data[idx]))
    
if n == 1:
    result = data[0]
else:
    dfs(1, data[0])
print(result)
        

