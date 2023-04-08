def solution(my_string):
    answer = 0
    a = my_string.split()
    answer = int(a[0])
    for i in range(1,len(a),2): 
        # print(a[i],type(a[i+1]))
        if a[i] == '+':
            answer += int(a[i+1])
        else:
            answer -= int(a[i+1])
    return answer