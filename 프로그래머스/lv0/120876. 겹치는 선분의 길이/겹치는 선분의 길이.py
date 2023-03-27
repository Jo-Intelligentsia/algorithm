def solution(lines):
    answer = 0
    lines[0][0] -= -1
    lines[1][0] -= -1
    lines[2][0] -= -1
    # print(lines)
    ls = []
    ls1 = []
    for i in range(len(lines)):
        lines[i][1] += 1
        
    for j in range(len(lines)):
        for k in range(lines[j][0],lines[j][1]):
            # print(k)
            if k not in ls:
                ls.append(k)
            else:
                ls1.append(k)
    print(ls)
    a = set(ls1)
    print(a)
                    
    return len(a)