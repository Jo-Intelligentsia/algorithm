T = int(input())
new = 0
# for i in range(T):
a = list(map(int,input().split()))
M = max(a)
for i in a:
    new += i/M * 100
print(new/T) 