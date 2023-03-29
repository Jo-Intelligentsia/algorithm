from math import gcd
# gcd 최대공약수 함수 사용
def solution(a, b):
    # b //= gcd(a,b) # a,b 의 최대공약수
    d = b//gcd(a,b)
    print(d)
    while d%2==0:
        d//=2
    while d%5==0:
        d//=5
    return 1 if d==1 else 2