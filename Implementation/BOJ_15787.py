import sys
train_num, m = map(int, input().split())

# [[0]*20 for _ in range(N)] != [[0]*20]*N, for _ in range를 쓰자
trains = [([0]*20) for _ in range(train_num + 1)]

answer = 0
answers = []

for _ in range(m):
    # input() 쓰면 시간 초과
    order = list(map(int, sys.stdin.readline().split()))
    
    if order[0] == 1:
        i = order[1]
        x = order[2]
        trains[i][x - 1] = 1

    elif order[0] == 2:
        i = order[1]
        x = order[2]
        trains[i][x - 1] = 0

    elif order[0] == 3:
        i = order[1]
        del trains[i][19]
        trains[i].insert(0, 0)

    elif order[0] == 4:
        i = order[1]
        del trains[i][0]
        trains[i].append(0)


answers = [True]*(train_num+1)
answers[0] = False
for i in range(1, train_num+1):
    if not answers[i]:
        continue
    for j in range(i+1, train_num+1):
        if answers[j] and trains[i] == trains[j]:
            answers[j] = False

print(sum(answers))
