string = input() # 단어 입력 받기 #단어가 5개면
s1 =[]
s2 =[]
s3 =[]
s4 =[]
for i in range(len(string)-2): # range(3) 012
    for j in range(i+1,len(string)-1): # range(1+i,4) 123
        # for k in range(i+2,len(string)): # range(2+i,5) 234
            if i == 0:
                # print(string[i],string[i+1:j+1],string[j+1:])
                s1.append(string[i])
                s2.append(string[i+1:j+1])
                s3.append(string[j+1:])
                s4.append(s1[0][::-1]+s2[0][::-1]+s3[0][::-1])
                s1.pop()
                s2.pop()
                s3.pop()
                # print(s4)
            elif i != 0:
                # print(string[:i+1],string[i+1:j+1],string[j+1:])
                s1.append(string[:i+1])
                s2.append(string[i+1:j+1])
                s3.append(string[j+1:])
                s4.append(s1[0][::-1]+s2[0][::-1]+s3[0][::-1])
                s1.pop()
                s2.pop()
                s3.pop()
                # print(s4)
            # elif j == k:
            #     print(string[i],string[i:j],string[k])
            # print(string[i],string[i:j],string[j:k])
    # print(i)
# print(s1,s2,s3)
s4.sort()
print(s4[0])