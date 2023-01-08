a , b , c = map(int,input().split())
d = 0
if a == b == c:
    d = 10000 + a* 1000
elif (a == b) or (a == c):
    d = 1000 + a *100
elif b == c:
    d = 1000+b*100
else:
    d = max(a,b,c)*100
print(d)