T = int(input())
for i in range(T):
    N = list(map(int,input().split()))
    cnt = 0
    
    avg = (sum(N[1:]))/N[0]
    for l in N[1:]:
        if l > avg:
            cnt +=1
        s = cnt/N[0] * 100
    print(f'{s:.3f}%')