N = input()
n = []
for i in N:
    n.append(i)

n.sort(reverse=True)
print(*n,sep='')