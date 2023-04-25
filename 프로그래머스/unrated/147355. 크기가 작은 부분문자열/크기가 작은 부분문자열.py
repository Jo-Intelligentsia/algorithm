def solution(t, p):
    answer = 0
    for i in range(len(t)):
        if i+len(p) > len(t):
            break
        if t[i:i+len(p)] <= p:
            answer +=1
        print(t[i:i+len(p)])
        j = t[i:i+len(p)]
        
    return answer