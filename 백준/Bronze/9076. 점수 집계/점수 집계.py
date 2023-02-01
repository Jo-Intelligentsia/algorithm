T = int(input())
for i in range(T):
    N = list(map(int,input().split()))
    N.remove(max(N))
    N.remove(min(N))
    N.sort()
    print('KIN' if N[2] - N[0] >= 4 else (sum(N)))