def is_in_range(n, start, end = 0):
    return start <= n <= end if end >= start else end <= n <= start
# 투 포인터 이용
def answer():
    answer = -1
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 시작, 끝 지점 나타내는 변수
    start = 0
    end = 0
    # 각 수의 개수를 저장하는 리스트
    num_cnt = [0] * 100001 #[0 for n in range(max(numbers) + 1)]
    # for i in range(n):
    #     num_cnt[numbers[i]] += 1
    num_cnt[numbers[end]] += 1
    while(start <= end):
        if (end == n):
            break
        # 숫자가 K개를 초과할 때
        if num_cnt[numbers[end]] > k:
            num_cnt[numbers[start]] -= 1
            start += 1
            #print(num_cnt, answer, end-start + 1)
        else:
            answer = max(answer, end-start + 1)
            end += 1
            num_cnt[numbers[end]] += 1
            # if num_cnt[numbers[end]] > k:
            #     num_cnt[numbers[start]] -= 1
            #     start += 1
            #     answer = max(answer, end-start + 1)
            #     print(num_cnt, answer, end-start + 1)
            # else:
            #     answer = max(answer, end-start + 1)
            #     end += 1
            #     num_cnt[numbers[end]] += 1
            #     print(num_cnt, answer)
            # else:
            #     start += 1
    print(answer)

if __name__ == "__main__":
    answer()