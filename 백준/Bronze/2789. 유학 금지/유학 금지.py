string = input()
s_del = 'CAMBRIDGE'
p = []

for i in string:
    if i not in s_del:
        p.append(i)
    else:
        pass

print(*p,sep='')