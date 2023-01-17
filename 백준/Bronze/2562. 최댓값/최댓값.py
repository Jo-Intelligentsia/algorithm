n_list = []
for i in range(1,10):
    num = int(input())
    n_list.append(num)
print(f'{max(n_list)}\n{n_list.index(max(n_list))+1}')