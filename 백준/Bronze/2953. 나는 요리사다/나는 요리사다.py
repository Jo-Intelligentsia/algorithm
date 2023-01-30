dict = {}
for i in range(1,6):
    a = map(int,input().split())
    dict[i]= sum(a)
print(max(dict, key=dict.get),max(dict.values()))