N,M = list(map(int,input().split())) # N 행 , M 열 
A = []
B = []
C = [[0]*M for _ in range(N)]
for i in range(2):      # A,B 를 위해 두번 반복
    for j in range(N):
        if i == 0:
            a = list(map(int,input().split()))
            A.append(a)
        elif i != 0:
            b = list(map(int,input().split()))
            B.append(b)
for i in range(N):
    for j in range(M):
        C[i][j] =A[i][j] + B[i][j]
for i in range(N):
    print(*C[i])