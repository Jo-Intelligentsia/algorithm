S = list(input())
word = list(input())
cnt = 0
st = 0
while True:
    if S == word:
        cnt +=1
        break
    elif len(S) < st + len(word):
        break
    if S[st:st+len(word)] == word:
        cnt += 1
        st += len(word)
    elif S[st:st+len(word)] != word:
        st += 1

print(cnt)