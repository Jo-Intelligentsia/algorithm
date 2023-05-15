def solution(id_list, report, k):
    answer = [0] * len(id_list)    # 전체 사람수 (신고 받기전 수)
    reports = {x : 0 for x in id_list} # 딕셔너리 사용 
    print(reports)
    for i in set(report): # 중복 제거 후 순회
        reports[i.split()[1]] += 1 # 신고 당한 사람의 신고횟수를 증가

    for i in set(report):
        if reports[i.split()[1]] >= k: # 정지인 유저일때
            answer[id_list.index(i.split()[0])] += 1 # 결과메일을 보내줄 id를 찾아 딕셔너리에 수를 증가
    return answer