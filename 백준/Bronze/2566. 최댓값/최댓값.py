N = [list(map(int,input().split())) for x in range(9)]
# print(N)
a = 0
b = 0
for i in range(9):
    for j in range(9):
        if N[0][0] < N[i][j]:
            N[0][0], N[i][j] = N[i][j], N[0][0]
            a = i
            b = j
        else:
            pass
            
print(N[0][0])
print(a+1,b+1,sep=' ')