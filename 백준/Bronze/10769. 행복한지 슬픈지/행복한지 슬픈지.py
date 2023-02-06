T = input()
happy = 0
sad = 0
for i in range(len(T)):
    if T[i] == ':':
        if T[i+1] == '-' and T[i+2] == ')':
            happy +=1
        elif T[i+1] == '-' and T[i+2] == '(':
            sad +=1
if happy > sad:             # happy 가 sad 보다 많으면      
    print('happy')          # happy 출력
elif happy == sad !=0 :     # happy 와 sad 의 횟수가 0이 아니고 같으면
    print('unsure')         # unsure 출력
elif happy == 0 and sad ==0:# happy 와 sad 가 모두 0이면
    print('none')           # none 출력
else:                       # 그외
    print('sad')            # sad 출력