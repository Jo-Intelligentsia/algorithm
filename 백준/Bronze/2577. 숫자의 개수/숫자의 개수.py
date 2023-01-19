total = 1
dict = {}
for i in range(3):
    num = int(input())
    total = total * num
for n in range(10):
    dict[n] = 0
for m in str(total):
    if dict[int(m)] in dict:
        dict[int(m)] += 1
for k in range(10):
    print(dict[k])