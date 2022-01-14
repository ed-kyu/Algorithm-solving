# 1개~50개의 수로 이루어져 있음 => 최대자리 2자리
# 9이하 수로만 이루어질 때 -> 1자리 수로만 이루어져 있음, 길이 = 숫자 개수
# 10이상 -> 길이 = 9 + 2*(숫자 개수 - 9)
import sys
def solution():
    nums = input()
    nums_len = len(nums)
    if nums_len < 10:
        max = nums_len
    elif nums_len >= 10:
        max = (nums_len - 9) // 2 + 9
    #print(max)
    cnt = [0] * (max +  1)
    #print(cnt)
    answer = []
    dfs(0, nums, answer, max, cnt, nums_len)

def dfs(index, nums, answer, max, cnt, nums_len):
    num = ''
    if index == nums_len:
        print(*answer)
        sys.exit()
    for i in range(index, index + 2):
        if i >= nums_len:
            break
        num += nums[i]
        if (int(num)) > max or cnt[int(num)] == 1:
            continue
        cnt[int(num)] += 1
        answer.append(int(num))
        dfs(i + 1, nums, answer, max, cnt, nums_len)
        cnt[int(num)] = 0
        answer.pop()

if __name__ == "__main__":
    solution()

