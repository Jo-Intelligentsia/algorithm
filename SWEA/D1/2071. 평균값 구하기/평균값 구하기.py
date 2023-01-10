T = int(input())
n_sum = 0
for t in range(1,T+1):
    number = list(map(int,input().split()))
    n_sum = sum(number)
    print(f'#{t} {n_sum/len(number):.0f}')