def solution():
    num = int(input())
    str_list = []
    for i in range(num):
        str_list.append(input())

    for i in str_list:
        reversed_str = "".join(reversed(i))
        if reversed_str in str_list:
            print(len(i), i[int(len(i)/2)])
            break

if __name__ == "__main__":
    solution()
