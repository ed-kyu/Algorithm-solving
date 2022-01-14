def cal_dist(item, pos_l, pos_r, pos, hand):
    X, Y = 0, 1
    dist_l = abs(pos[pos_l][X] - pos[item][X]) + abs(pos[pos_l][Y] - pos[item][Y])
    dist_r = abs(pos[pos_r][X] - pos[item][X]) + abs(pos[pos_r][Y] - pos[item][Y])
    # 거리가 같으면
    if dist_l == dist_r:
        return 'R' if hand == 'right' else 'L'
    return 'R' if dist_l > dist_r else 'L'


def solution(numbers, hand):
    answer = ''
    position = {1:(0, 0), 2:(0, 1), 3:(0, 2),
                4:(1, 0), 5:(1, 1), 6:(1, 2),
                7:(2, 0), 8:(2, 1), 9:(2, 2),
                '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    left, right = set([1,4,7]), set([3,6,9])
    pos_l = '*'
    pos_r = '#'
    for item in numbers:
        if item in left:
            answer += 'L'
            pos_l = item
        elif item in right:
            answer += 'R'
            pos_r = item
        else:
            answer += cal_dist(item, pos_l, pos_r, position, hand)
            if answer[-1] == 'L':
                pos_l = item
            else :
                pos_r = item
    return answer