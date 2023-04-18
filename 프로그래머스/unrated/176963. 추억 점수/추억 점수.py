def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    for j in range(len(photo)):
        for k in range(len(photo[j])):
            if photo[j][k] in dic.keys():
                photo[j][k] = dic[photo[j][k]]
            else:
                photo[j][k] = 0
    for i in photo:
        answer.append(sum(i))
    return answer

