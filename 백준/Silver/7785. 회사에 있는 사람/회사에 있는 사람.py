n = int(input())
dict = {}
for i in range(n):
    person = input().split()
    if 'enter' in person:
        dict[person[0]] = person[1]
    elif 'leave' in person:
        del dict[person[0]]
# sorted(dict.keys(), reverse=True)
# print(*dict.keys(),sep='\n')
for people in sorted(dict.keys(),reverse=True):
    print(people)