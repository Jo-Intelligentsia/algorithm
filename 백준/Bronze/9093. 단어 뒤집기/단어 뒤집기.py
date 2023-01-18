T = int(input())

for i in range(T):
    a = list(input().split())
    for t in a:
        print(t[::-1], end=' ')
    print()