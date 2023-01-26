T = int(input())
for l in range(1,T+1):
    PS = input()
    while len(PS) > 1:
        a = PS.replace('()','*')
        PS = a.replace('*','')
        if '()' not in PS:
            break
    if len(PS) ==0:
        print('YES')
    else:
        print('NO')