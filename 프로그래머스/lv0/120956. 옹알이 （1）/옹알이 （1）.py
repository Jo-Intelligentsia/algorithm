from itertools import permutations

def solution(babbling):
    answer = 0
    
    perm = [] # 가능한 모든 말
    for i in range(4): 
        perm.append(list(permutations(["aya", "ye", "woo", "ma"], i+1)))
        
    for i in range(len(perm)): # 튜플로 구성된 순열을 하나의 문자열로 바꿈
        for j in range(len(perm[i])):
            perm[i][j] = ''.join(list(perm[i][j]))

    for b in babbling: # 발음할 수 있는 단어인지 확인
        for i in range(len(perm)):
            if b in perm[i]:
                answer += 1
                
    return answer