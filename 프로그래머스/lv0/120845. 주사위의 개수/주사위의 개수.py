def solution(box, n):
    answer = 0
    a = box[0]//n # 가로면 박스 수
    b = box[1]//n # 세로면 박스 수
    c = box[2]//n # 높이면 박스 수
    answer = a*b*c
    return answer