new = 0
cnt = 0
N = int(input())
n1 = N
while True:
    N = (N//10 + N%10)%10 + (N%10 * 10)
    cnt += 1 
    if n1 == N:
        break
print(cnt)