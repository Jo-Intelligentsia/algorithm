N = int(input())
n_sum = 0
for i in range(N):
    a = int(input())
    n_sum += a
if n_sum > N//2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')