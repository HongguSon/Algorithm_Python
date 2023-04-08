# 5658번 보물상자 비밀번호
def hex_to_10(hex_number: str):
    return int(hex_number, 16)


T = int(input())

for t in range(1, T+1):
    # print(t)
    n, k = map(int, input().split())
    nums = list(input())
    # print(n, k, nums)
    num_list = []
    for j in range(n):
        nums = list(nums[-1]) + nums[0:-1]
        for l in range(0, n, n//4):
            num_list.append(''.join(nums[l:l+(n//4)]))
        # print(num_list)
    num_list = list(set(num_list))

    for i in range(len(num_list)):
        num_list[i] = hex_to_10((num_list[i]))

    num_list.sort(reverse=True)
    # print(num_list)
    print('#{} {}'.format(t, num_list[k-1]))






