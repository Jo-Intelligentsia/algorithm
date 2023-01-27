T = int(input())
ls = []
for i in range(T):
    word = input()
    if word not in ls:
        ls.append(word)
    else:
        pass
ls.sort(key=lambda x : (len(x),x))
print(*ls,sep='\n')