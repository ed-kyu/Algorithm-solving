T = int(input())

for _ in range(T):
    a, b = map(str, input().split())
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    if sorted_a == sorted_b:
        print(a, '&', b, 'are anagrams.')
    else:
        print(a, '&', b, 'are NOT anagrams.')


# T = int(input())

# for _ in range(T):
#     a, b = input().split()
#     flag = False
#     if len(a) == len(b):
#         test_b = b
#         for i in a:
#             if i not in test_b:
#                 flag = False
#                 break
#             else:
#                 test_b = list(test_b)
#                 test_b.remove(i)
#                 test_b = ''.join(test_b)
#                 flag = True
#     if flag == True:
#         print(a, '&', b, 'are anagrams.')
#     else:
#         print(a, '&', b, 'are NOT anagrams.')