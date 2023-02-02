N = int(input())  # 높이를 측정한 개수
P = list(map(int,input().split())) # 높이의 숫자
a = 0 # 비교횟수
h = 0 # 높이
ls = [] # 오르막의 높이
while True:
    if P[a]-P[a+1] < 0: # 오르막이면
        h += P[a+1]-P[a] # 높이에 추가
    else: # 오르막이 아니면
        ls.append(h)
        h = 0 # 높이를 0으로 리셋
    a +=1 # 비교 횟수 추가
    
    if a == N-1: # 비교 횟수가 N-1 되면 while 끝
        ls.append(h)
        break
print(max(ls))