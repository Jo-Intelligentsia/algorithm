R, C, N = map(int,input().split())
a = 0
b = 0
if R%N !=0:
    a = R//N +1
    if C%N !=0:
        b = C//N +1
    else:
        b = C//N
else:
    a = R//N
    if C%N !=0:
        b = C//N +1
    else:
        b = C//N
print(a*b)