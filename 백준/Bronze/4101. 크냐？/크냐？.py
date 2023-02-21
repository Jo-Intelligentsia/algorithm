while True:
    n,m = map(int,input().split())
    if n >m:
        print('Yes')
    elif n == 0 and m== 0:
        break
    else:
        print('No')