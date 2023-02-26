while True:
    s = list(map(str,input().split()))
    if ['#', '0', '0'] == s:
        break
    else:
        if int(s[1]) > 17 or int(s[2]) >= 80:
            print(s[0],'Senior')
        else:
            print(s[0],'Junior')