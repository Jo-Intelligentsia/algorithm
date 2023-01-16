N, X = map(int,input().split())
A = list(map(int,input().split()))
min_A = []

for i in A:
    if i < X:
        min_A.append(i)

print(*min_A)