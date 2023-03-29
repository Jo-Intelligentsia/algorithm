def solution(id_pw, db):
    answer = ''
    for i in db:
        if i == id_pw:
            answer = 'login'
            break
        elif i[0] == id_pw[0]  and i[1] != id_pw[1]:
            answer = 'wrong pw'
    if answer =='':
        answer = 'fail'
    return answer