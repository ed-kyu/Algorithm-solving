import sys
             
def check(num):
    flag = True
    for i in range(len(num)):
        if num[i] == num[-(i + 1)]:
            pass
        else:
            flag = False
            break
    return flag

while(1):
    num = input()
    min_palin_num = 0
    total_num = len(num)
    zero_num = len(num) - len(str(int(num)))
    if num == '0':
        sys.exit()
    else:
        while(1):
            if check(num) == True:
                print(min_palin_num)
                break
            else:
                num = str(int(num) + 1)
                zero_num = total_num - len(str(int(num)))
                for i in range(zero_num):
                    num = '0' + num
                min_palin_num += 1