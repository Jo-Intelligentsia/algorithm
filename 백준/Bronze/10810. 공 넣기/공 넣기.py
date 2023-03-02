N,M = map(int,input().split())

m = [0 for _ in range(N)]
# print(m)
for a in range(M):
    i,j,k = map(int,input().split())
    for b in range(i-1,j):
        m[b] = k
print(*m)