def check(n):
    if n != 0 and n != 1:
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True
    else:
        return False

def solve(n):
    for i in range(n, 4*(10**10)+1):
        if check(i):
            return i

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
