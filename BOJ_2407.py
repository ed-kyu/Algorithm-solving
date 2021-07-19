# 팩토리얼 구현
# 나눗셈 할 때 소숫점 버리는 연산 ==>  // 사용
import math

def solution():
    n, m = map(int, input().split())
    n_factorial = math.factorial(n)
    m_facorial = math.factorial(m)
    n_minus_m_factorial = math.factorial(n-m)
    answer = n_factorial // (m_facorial * n_minus_m_factorial)
    print(answer)

if __name__ == "__main__":
    solution()