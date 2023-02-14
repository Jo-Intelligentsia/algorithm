mush_ = [int(input()) for x in range(10)]
score = 0
for i in range(len(mush_)):
    if score < 100:             # 합이 100 전까지 진행
        score += mush_[i]       # 100 가까운 수까지 합산
        if score >= 100:        # 총합이 100보다 크거나 같으면
            if score-100 <= 100-(score-mush_[i]):      # 총합-100 이 100-전 회차 총합 보다 작거나 같으면
                print(score)    # 100이 넘어도 출력
                break
            else:               # 100 전의 숫자가 작을땐 전회차 총합 출력
                print(score-mush_[i])
                break
if score < 100:
    print(score)