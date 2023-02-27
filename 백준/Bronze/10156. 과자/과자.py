# 10156 과자
a,b,c = map(int,input().split())
d = a*b-c
if d < 0:
    print(0)
else:
    print(d)