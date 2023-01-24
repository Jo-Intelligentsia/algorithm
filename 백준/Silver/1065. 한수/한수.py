N = int(input())
cnt = 0
for i in range(1,N+1):
    if i < 10:
        cnt += 1
    elif i < 100:
        cnt += 1
    elif i <= 1000:
        if i//100 - i//10%10 == i//10%10 - i%10:
            cnt +=1
print(cnt)