a,b,c = map(int,input().split())
d = int(input())

b = d//60+b # 분
c = d%60+c # 초

if c >= 60:
    c -= 60
    b += 1
if b>= 60:
    a += b//60
    b -= (b//60*60)
    
if a >= 24:
    a -= a//24*24
print(a,b,c)