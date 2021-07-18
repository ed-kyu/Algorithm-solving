# 투 포인터 이용
def answer():
    answer = 0
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 시작, 끝 지점 나타내는 변수
    start = 0
    end = 0
    # 각 수의 개수를 저장하는 리스트
    num_cnt = [0 for n in range(max(numbers) + 1)]
    while(end < n):
        # 숫자가 K개를 초과할 때
        if num_cnt[numbers[end]] > k:
            num_cnt[numbers[start]] -= 1
            start += 1
            if num_cnt[numbers[end]] == k:
                end += 1
        else:
            num_cnt[numbers[end]] += 1
            if num_cnt[numbers[end]] > k:
                num_cnt[numbers[start]] -= 1
                start += 1
            else:
                end += 1
                answer = max(answer, end-start)
    print(answer)

if __name__ == "__main__":
    answer()