N = int(input())
n = [[] for i in range(N)]
# print(n)
for _ in range(N):
    x , y = map(int,input().split())
    n[_]=x,y
n.sort()
for i in n:
    print(*i)