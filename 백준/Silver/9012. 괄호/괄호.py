T = int(input())

for i in range(T):
    ls = []
    ps = input()
    for l in ps:
        if l == '(':
            ls.append('(')
        elif l == ')':
            if len(ls) >= 1 :
               ls.pop()
            elif len(ls) < 1 :
                ls.append(')')
                break

    if len(ls) == 0:
        print('YES')
    else:
        print('NO')