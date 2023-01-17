N = int(input())
n_list = []
for i in range(N):
    num = int(input())
    n_list.append(num)
    n_list.sort()
print(*n_list,sep='\n')