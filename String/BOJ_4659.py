import sys

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    pwd = input()
    vowel_check = 0
    consonant_check = 0
    flag = False
    if pwd == 'end':
        sys.exit()
    for idx, word in enumerate(pwd):
        if word in vowels:
            vowel_check += 1
            consonant_check = 0
            flag = True
        else:
            vowel_check = 0
            consonant_check += 1
        if vowel_check >= 3 or consonant_check >= 3:
            flag = False
            break
        if idx >= 1 and idx < len(pwd) and pwd[idx] == pwd[idx - 1]:
            if pwd[idx] not in 'eo':
                flag = False
                break
            else:
                flag = True
                continue
    if flag == True:
        print(f'<{pwd}> is acceptable.')
    elif flag == False:
        print(f'<{pwd}> is not acceptable.')

            
