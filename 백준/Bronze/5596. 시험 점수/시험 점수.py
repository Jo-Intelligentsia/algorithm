# 5596 시험점수
S = map(int,input().split())
T = map(int,input().split())
S = sum(S)
T = sum(T)
if S >= T:
    print(S)
else:
    print(T)