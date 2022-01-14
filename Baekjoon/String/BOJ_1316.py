import sys
input = sys.stdin.readline
n = int(input())
answer = 0
for _ in range(n):
    
    word = input().split()
    result = ''
    result += word[0][0]
    for idx in range(1, len(word[0])):
        if word[0][idx-1] != word[0][idx]:
            result += word[0][idx]
    result2 = ''
    for idx in range(len(result)):
        if result[idx] in result2:
            answer -= 1
            break
        else:
            result2 += result[idx]
    answer += 1
print(answer)