s = input().upper()
ls =list(set(s))
cnt = []
for i in ls:
    c = s.count(i) # 입력값을 차례로 반복, ls를 하나씩 c에 추가
    cnt.append(c) # cnt 에 값을 하나씩 추가
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(ls[cnt.index(max(cnt))])