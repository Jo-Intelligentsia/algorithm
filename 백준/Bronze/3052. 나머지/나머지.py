cnt = 0
ls = []
for i in range(10):
    num = int(input())
    if num%42 not in ls:
        ls.append(num%42)
    elif num%42 in ls:
        pass
print(len(ls))