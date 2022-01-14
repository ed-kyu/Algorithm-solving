import sys
t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split()))
    a_list = list(map(int, sys.stdin.readline().split()))
    b_list = list(map(int, sys.stdin.readline().split()))
    a_list.sort()
    b_list.sort()
    a_idx = b_idx = 0
    count = 0
    while (a_idx < len(a_list)):
        while (b_idx < len(b_list)):
            if (a_list[a_idx] <= b_list[b_idx]):
                count += b_idx
                break
            elif (b_idx == len(b_list) - 1):
                count += b_idx+1
                break
            else:
                b_idx += 1
        a_idx += 1
    print(count)
