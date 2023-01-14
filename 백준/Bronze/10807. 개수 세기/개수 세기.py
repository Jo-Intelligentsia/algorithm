N = int(input())

a = map(int,input().split())
b = int(input())
c = 0
for i in a:
    if b == i:
        c += 1
print(c)
