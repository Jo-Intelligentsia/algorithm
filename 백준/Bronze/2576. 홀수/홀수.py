ls = []
for i in range(7):
    num = int(input())
    if num%2 == 1:
        ls.append(num)
    else:
        pass
if len(ls) == 0:
    print(-1)
else:
    print(sum(ls))
    print(min(ls))