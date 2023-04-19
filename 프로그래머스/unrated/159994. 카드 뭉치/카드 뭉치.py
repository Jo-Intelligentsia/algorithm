def solution(cards1, cards2, goal):
    answer = []
    for i in goal:
        if len(cards1) != 0:
            if cards1[0] == i:
                answer.append(cards1[0])
                del cards1[0]
        if len(cards2) !=0:
            if cards2[0] == i:
                answer.append(cards2[0])
                del cards2[0]
    if answer == goal:
        return 'Yes'
    else:
        return 'No'
