def solution(num_list, n):
    answer = ([[] for _ in range(len(num_list)//n)])
    for i in range(len(answer)):
        for j in range(n):
            answer[i].append(num_list[0])
            num_list.remove(num_list[0])
    return answer