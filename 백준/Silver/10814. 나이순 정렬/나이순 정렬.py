N = int(input())
n = []
for _ in range(N):
    x , y = input().split()
    n.append([int(x),y])
    
n.sort(key=lambda x: x[0])
for i in n:
    print(int(i[0]),i[1])