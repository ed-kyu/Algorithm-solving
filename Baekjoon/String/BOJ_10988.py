# BOJ_10988

word = input()
n = len(word)
flag = 0
for i in range(int(n/2) + 1):
    if word[i] != word[-i-1]:
        print(0)
        flag = 1
        break

if flag == 0:
    print(1)
    