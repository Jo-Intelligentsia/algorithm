T = input()
ls = []
while True:
    a = input()
    if a == '문제':
        ls.append('문제')
    elif a == '고무오리':
        if '문제' in ls:
            ls.pop()
        else:
            ls.append('문제')
            ls.append('문제')
    if a == '고무오리 디버깅 끝':
        break
if len(ls) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')
