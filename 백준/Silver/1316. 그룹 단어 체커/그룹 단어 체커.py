import sys

T = int(sys.stdin.readline())
cnt = 0
for i in range(T):
    s = sys.stdin.readline()
    ls =[]
    s_n =0
    for l in s:
        s_n +=1
        if l not in ls:
            ls.append(l)
        elif l in ls:
            if ls[-1] == l:
                ls.append(l)
            elif ls[-1] != l:
                ls.pop()
                s_n -=1
    if s_n == len(ls):
        cnt +=1
print(cnt)

