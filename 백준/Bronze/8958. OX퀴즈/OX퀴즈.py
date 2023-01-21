T = int(input())


for i in range(T):
    s = input()
    cnt = 0
    total = []
    for n in s:
        
        if 'O' == n:
            cnt += 1
            total.append(cnt)
        else:
            cnt = 0
            
    print(sum(total))