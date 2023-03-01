T = int(input())
L = list(map(int,input().split()))
cnt = 0
for i in L:
    if i == T:
        cnt +=1
    else:
        pass
print(cnt)