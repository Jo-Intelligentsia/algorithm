people = 0
max_ = 0
for i in range(4):
    out_, in_ = list(map(int,input().split()))
    people -= out_ 
    people += in_
    if max_ < people:
        max_ = people
print(max_)