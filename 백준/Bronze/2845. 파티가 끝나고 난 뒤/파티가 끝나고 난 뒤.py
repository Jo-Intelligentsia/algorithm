a,b = map(int,input().split())
c = list(map(int,input().split()))
ls=[]
d = a * b

for i in range(5):
    ls.append(c[i]-d)

print(*ls)