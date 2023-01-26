C = int(input())
N = list(map(int,input().split()))
S = []
cnt = 0
for i in N:
    if i not in S:
        S.append(i)
    elif i in S:
        cnt += 1

print(cnt)