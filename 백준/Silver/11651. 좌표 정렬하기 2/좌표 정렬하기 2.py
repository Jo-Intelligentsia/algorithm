N = int(input())
n = [[] for i in range(N)]
for _ in range(N):
    x , y = map(int,input().split())
    n[_]=[y,x]
n.sort()
for i in n:
    print(i[1],i[0])