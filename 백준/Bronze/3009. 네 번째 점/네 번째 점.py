n_list = []
n4 = []
for i in range(3):
    num = input().split()
    n_list = n_list + num

if n_list[0] == n_list[2]:
    n4.append(n_list[4])
elif n_list[0] == n_list[4]:
    n4.append(n_list[2])
elif n_list[2] == n_list[4]:
    n4.append(n_list[0])
if n_list[1] == n_list[3]:
    n4.append(n_list[5])
elif n_list[1] == n_list[5]:
    n4.append(n_list[3])
elif n_list[3] == n_list[5]:
    n4.append(n_list[1]) 
    

print(*n4)