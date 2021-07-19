# 팩토리얼 구현
# math 라이브러리 사용하지 않고 작성하는 법 ==> reduce 이용 (시간 제일 오래 걸림)
# 나눗셈 할 때 소숫점 버리는 연산 ==>  // 사용
from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

def solution():
    n, m = map(int, input().split())
    answer = factorial_reduce(n) // (factorial_reduce(m) * factorial_reduce(n-m))
    print(answer)

if __name__ == "__main__":
    solution()