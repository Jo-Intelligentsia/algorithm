N, M = map(int,input().split())  # N = 듣지 못한 사람, M = 보지 못한 사람수
# for i in N:
a = [input() for i in range(N)]
b = [input() for j in range(M)]
c = list(set(a) & set(b))
c.sort()
print(len(c),*c,sep='\n')