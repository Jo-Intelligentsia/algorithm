N = int(input())
y = 0
s = 0
while True:
    y +=1
    if '666' in str(y):
        s += 1
    if N == s:
        print(y)
        break