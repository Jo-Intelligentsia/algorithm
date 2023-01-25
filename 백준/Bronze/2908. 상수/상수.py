N = input().split()
ls = []
for i in N:
    ls.append(i[::-1])
print(max(ls))