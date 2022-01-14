def solution(board, moves):
    answer = []
    num = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:       
                if len(answer) >= 1:
                    if answer[-1] == board[j][i - 1]:
                        answer = answer[:-1]
                        num += 1
                    else:
                        answer.append(board[j][i - 1])
                else:
                    answer.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
    return num*2