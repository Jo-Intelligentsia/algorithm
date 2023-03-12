def solution(n):
    s = 2
    h = []
    while True:
        if s == n:
            if s not in h:
                h.append(s)
            break
        if n%s == 0:
            n //= s
            if s not in h:
                h.append(s)
            else:
                pass
        elif n%s != 0:
            s += 1
    return h