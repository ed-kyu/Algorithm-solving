T = int(input())

for i in range(T):
    nums = []
    mid_res = []

    M = int(input())

    for _ in range(M//10 + 1):
        nums.extend(list(map(int, input().split())))

    result = (int(M/2 + 1))
    for i in range(1, M+1, 2):
        mid_res.append(sorted(nums[:i])[i//2])

    print(result)
    for i in range(M//20 + 1):
        print(*mid_res[10*i:10*i+10])

# min-heap, max-heap 이용?