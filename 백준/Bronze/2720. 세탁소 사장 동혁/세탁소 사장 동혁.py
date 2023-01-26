T = int(input())
for i in range(T):
    money = int(input()) 
    ls = []
    if money >= 25:
        ls.append(money//25)
        money -= ls[0] * 25
    elif money//25 == 0:
        ls.append(0)
    if money >= 10:
        ls.append(money//10)
        money -= ls[1] * 10
    elif money//10 == 0:
            ls.append(0)
    if money >= 5:
        ls.append(money//5)
        money -= ls[-1] * 5
    elif money//5 == 0:
            ls.append(0)
    if money > 0:
        ls.append(money//1)
        money -= ls[-1]
    elif money//1 == 0:
            ls.append(0)

    print(*ls)
