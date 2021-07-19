def solution():
    N = int(input())
    answer = -1
    for i in range(int(N / 5) + 1):
        five_kg = i
        three_kg = int((N - i * 5) / 3)
        if five_kg * 5 + three_kg * 3 == N:
            answer = five_kg + three_kg
    print(answer)

if __name__ == "__main__":
    solution()