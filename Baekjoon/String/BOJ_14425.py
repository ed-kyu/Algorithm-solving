import sys
n, m = list(map(int, input().split()))
set_s = []
count = 0
for _ in range(n):
    set_s.append(sys.stdin.readline())
for _ in range(m):
    word = sys.stdin.readline()
    if word in set_s:
        count += 1
print(count)

# str = sys.stdin.read().split()
# S, command = set(str[:N]), str[N:]
# print(sum(1 for i in command if i in S))