T = int(input())
a = [' ']*T
N = len(a)
new_a = ['*' for _ in range(N)]
print(*new_a,sep='')
for i in range(N):
    # 새로운 리스트에 
    new_a[i-N] = a[i]
    print(*new_a,sep='')
    if i == N-2:
        break