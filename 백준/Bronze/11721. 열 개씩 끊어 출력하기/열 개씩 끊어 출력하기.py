word = input()
cnt = 0
word1 = ''
for i in word:
    # print(i)
    cnt += 1
    word1 += i
    if cnt == 10:
        cnt = 0
        print(word1)
        word1 = ''  
print(word1)