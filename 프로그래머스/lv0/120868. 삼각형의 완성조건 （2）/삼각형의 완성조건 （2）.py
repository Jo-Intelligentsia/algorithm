def solution(sides):
    cnt = 0
    a = max(sides) - min(sides) + 1
    while True:
        if a <= max(sides):
            cnt +=1
            a +=1
        else:
            break
    b = sum(sides)
    c = max(sides)
    while True:
        c += 1
        if c < b:
            cnt += 1
        else:
            break
    return cnt