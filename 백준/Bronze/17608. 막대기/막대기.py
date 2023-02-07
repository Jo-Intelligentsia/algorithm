import sys

n = int(sys.stdin.readline()) # 막대기 개수
stack = [int(sys.stdin.readline()) for _ in range(n)] # 입력값 스택에 삽입
last = stack.pop() # 처음 보이는 막대기 (마지막으로 삽입한 막대기)
cnt = 1 # 보이는 막대기의 수

# 반복문을 통해 막대기의 높이를 확인
for i in range(1, n):
    now = stack.pop() # 현재 마지막 막대기
    # 현재 마지막 막대기가 처음 보였던 막대기보다 높으면
    if now > last:
        cnt += 1 # 카운트
        last = now # 처음 보였던 막대기를 현재 마지막 막대기로 초기화

# 보이는 막대기의 수 출력
print(cnt)
