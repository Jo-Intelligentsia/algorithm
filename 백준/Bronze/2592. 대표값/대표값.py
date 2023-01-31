total=0
dict ={}

for i in range(10):
    s = int(input())
    total += s
    if s not in dict:
        dict[s] = 1
    elif s in dict:
        dict[s] += 1
avg = total // 10
print(avg)
print(max(dict,key=dict.get))