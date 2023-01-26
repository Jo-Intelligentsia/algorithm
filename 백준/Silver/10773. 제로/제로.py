import sys

K = int(sys.stdin.readline())
ls = []
cnt = 0
for i in range(K):
    N = input()
    if '0' == N:
        ls.pop()
        # print(ls)
    if '0' != N:
        ls.append(N)
for l in ls:
    cnt = cnt + int(l)
print(cnt)