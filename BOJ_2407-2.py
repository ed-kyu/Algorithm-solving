# 팩토리얼 구현
# math 라이브러리 사용하지 않고 작성하는 법 ==> 재귀함수 이용 (시간 차이는 없음...)
# 나눗셈 할 때 소숫점 버리는 연산 ==>  // 사용

def factorial_recursive(n):
    return n * factorial_recursive(n - 1) if n > 1 else 1

def solution():
    n, m = map(int, input().split())
    answer = factorial_recursive(n) // (factorial_recursive(m) * factorial_recursive(n-m))
    print(answer)

if __name__ == "__main__":
    solution()