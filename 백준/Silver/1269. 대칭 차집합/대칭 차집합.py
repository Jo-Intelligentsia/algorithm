
T = map(int,input().split())
A = map(int,input().split())
B = map(int,input().split())
C = set(B) ^ set(A)
print(len(C))