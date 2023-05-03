#14503번

n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(n) ]
import sys
sys.setrecursionlimit(10**9)


def move(r,c,d):
    if d == 0:
        return r-1, c
    elif d == 1:
        return r, c+1
    elif d == 2:
        return r+1, c
    elif d == 3:
        return r, c-1


def clean(r,c,d):
    
    def op1(r,c,d):
        global result
        matrix[r][c] = 2
        result += 1
        clean(r,c,d)
    
    def op2(r,c,d):
        d = (d+2)%4
        r1, c1 = move(r,c,d)
        if matrix[r1][c1] == 1:
            return
        else:
            d = (d+2)%4
            clean(r1,c1,d)
    
    def op3(r,c,d):
        d = (d+3)%4
        r1, c1 = move(r,c,d)
        if matrix[r1][c1] == 0:
            clean(r1,c1,d)
        else:
            op3(r,c,d)
        
    if matrix[r][c] == 0:
        op1(r,c,d)
        
    elif matrix[r][c] == 2:
        #2번 동작
        if matrix[r+1][c] == 0 or matrix[r-1][c] == 0 or \
            matrix[r][c+1] == 0 or matrix[r][c-1] == 0:
                op3(r,c,d)
        else:
            op2(r,c,d)
            
result = 0
clean(r,c,d)
print(result)            
    
        