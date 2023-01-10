T = int(input())

for t in range(1,T+1):
    a, b = map(int,input().split())
    m, n = divmod(a,b)
    print(f'#{t} {m} {n}')