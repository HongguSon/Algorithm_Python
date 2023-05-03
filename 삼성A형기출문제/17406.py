import copy
import itertools

def rotation(r,c,s,array):
    temp_array = [ array[r-s-1+i][c-s-1:c+s] for i in range(2*s+1) ]
    result = [[0]*(2*s+1) for _ in range(2*s+1)]
    for i in range(2*s+1):
        if i == 0:
            temp = [temp_array[1][0]]
            temp.extend(temp_array[0][:-1])
            result[0] = temp
        elif 0 < i < s:
            temp = temp_array[i+1][:i+1]
            temp.extend(temp_array[i][i:-(i+1)])
            temp.extend(temp_array[i-1][-i:])
            result[i] = temp
        elif i == s:
            temp = temp_array[i+1][:s]
            temp.append(temp_array[i][s])
            temp.extend(temp_array[i-1][-s:])
            result[i] = temp
        elif s < i < 2*s:
            temp = temp_array[i+1][:(2*s-i)]
            temp.extend(temp_array[i][2*s-i+1:-(2*s-i)])
            temp.extend(temp_array[i-1][-i+1:])
            result[i] = temp
        else:
            temp = temp_array[-1][1:]
            temp.append(temp_array[-2][-1])
            result[i] = temp
      
    a = 0
    for i in range(r-s-1, r+s):
        array[i][c-s-1:c+s] = result[a]
        a += 1
        
    return array

N, M, K = map(int, input().split())
or_array = [list(map(int, input().split())) for _ in range(N)]

rotate = []
for _ in range(K):
    rotate.append(list(map(int, input().split())))

rotate_set = itertools.permutations(rotate)

# answer = 987654321
answer = []
for rotates in list(rotate_set):
    print(rotates)
    rotate_array = copy.deepcopy(or_array)
    # print('시작배열\n',rotate_array)
    for rotate_element in rotates:
        rotate_array = rotation(rotate_element[0], rotate_element[1], rotate_element[2], rotate_array)
        # print('회전이후배열\n',rotate_array)
    for i in range(N):
        # if answer > sum(rotate_array[i]):
        #     answer = sum(rotate_array[i])
        answer.append(sum(rotate_array[i]))
# print(answer)
print(int(min(answer)))
