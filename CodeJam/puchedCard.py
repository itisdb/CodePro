def ascii(R,C):
    #for the first row
    for i in range(C*2+1):
        if i<2:
            print(".",end="")
        else:
            if i%2==0:
                print("+",end="")
            else:
                print("-",end="")
    print("")
    #for the second row
    for i in range(C*2+1):
        if i<2:
            print(".",end="")
        else:
            if i%2==0:
                print("|",end="")
            else:
                print(".",end="")
    print("")
    #for the rest of the rows
    for i in range(R*2-1):
        if i%2==0: # for the borders
            for j in range(C*2+1):
                if j%2==0:
                    print("+",end="")
                else:
                    print("-",end="")
            print("")
        else: # for the middle
            for j in range(C*2+1):
                if j%2==0:
                    print("|",end="")
                else:
                    print(".",end="")
            print("")

testcase = int(input())
R,C=[],[]
for i in range(testcase):
    x = input().split(" ")
    R.append(int(x[0]))
    C.append(int(x[1]))
for i in range(testcase):
    print("Case #"+str(i+1)+":")
    ascii(R[i],C[i])
