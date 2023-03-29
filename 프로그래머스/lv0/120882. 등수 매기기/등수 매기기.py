def solution(score):
    avg = []
    for i in score:
        avg.append(sum(i)/2) # 평균
    score_avg = sorted(avg, reverse=True) # 평균을 큰 값부터 내림차순 정렬

    answer =[] # 등수
    for i in avg:
        answer.append(score_avg.index(i)+1) # index는 맨 앞에 위치한 요소의 인덱스 번호를 리턴
    
    return answer