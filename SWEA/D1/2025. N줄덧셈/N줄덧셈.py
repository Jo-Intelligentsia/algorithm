N = int(input()) # 주어진 숫자를 받기 위해 int를 사용
total = 0 # 모든 수를 던한 값을 저장하기 위한 변수
for i in range(1,N+1): # 1부터 N의 숫자까지 반복
    total += i # total 변수에 반복되는 i를 합산
print(total) # total 출력