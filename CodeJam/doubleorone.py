def allCharactersSame(s):
    s1 = []
    for i in range(len(s)):
        s1.append(s[i])
    s1 = list(set(s1))
    if(len(s1) == 1):
        return True
    else:
        return False

t=int(input())
for _ in range(t):
    word = input()
    #getting the double or one thing
    ans =''
    if allCharactersSame(word):
        ans = word
    else:
        dob = word[0]+word[0]
        temp=[word[0], dob]
        for i in range(1,len(word)):
            temp1 = []
            for j in range(len(temp)):
                temp1.append(temp[j]+word[i])
                temp1.append(temp[j]+word[i]+word[i])
            temp = temp1
        temp=sorted(temp)
        ans=temp[0]

    print("Case #"+str(_+1)+": "+ans)