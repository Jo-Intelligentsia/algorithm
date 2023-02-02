M = int(input()) # 컵의 위치를 바꾸는 횟수
b = 1 # 볼의 처음 위치
for i in range(M): # M 만큼 반복
    x,y = map(int,input().split()) # 컵 위치를 바꿀 x,y 입력
    if x == b: # x 가 b 와 같으면 b 를 y 로 변경 (볼의 위치 변경)
        b = y
    elif y == b: # y가 b 와 같으면 b 를 x 로 변경 (볼의 위치 변경)
        b = x
print(b)