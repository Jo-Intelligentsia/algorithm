TB = input()
cnt = 0
ls = []
ls1 = []
for i in TB:
    cnt += 1
    if i == '@':
        ls.append(i)
    elif i == '(':
        break
for t in TB[cnt:]:
    if t == '@':
        ls1.append(t)
print(len(ls),len(ls1))