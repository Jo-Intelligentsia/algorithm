def solution(s):
    d = {}  # 문자별 이전 위치를 저장할 딕셔너리
    result = []  # 결과 리스트
    
    for i, c in enumerate(s):
        if c in d:  # 이전에 나온 문자라면
            result.append(i - d[c])  # 가장 가까운 위치 계산하여 결과 리스트에 추가
        else:
            result.append(-1)  # 이전에 나온 문자가 없으면 -1을 결과 리스트에 추가
        d[c] = i  # 딕셔너리에 문자 c의 위치를 업데이트
        
    return result