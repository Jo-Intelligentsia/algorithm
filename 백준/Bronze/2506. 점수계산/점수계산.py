N = int(input())
score_total = 0 # 연속된 O 의 점수
total_sum = 0 # 점수 총합
num = 0 # 횟수
score = list(map(int,input().split()))

for i in score:  
    if i == 1:
        score_total += 1
    else:
        score_total = 0
    total_sum = total_sum + score_total
print(total_sum)