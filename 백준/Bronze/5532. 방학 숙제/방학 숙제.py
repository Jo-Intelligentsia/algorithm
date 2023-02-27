L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A%C !=0:
    A = A//C +1
else:
    A = A//C
if B%D !=0:
    B = B//D +1
else:
    B = B//D
if A >= B:
    L -= A
else:
    L -= B

print(L)