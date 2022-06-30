def stringSort(msg_given):
    msg_alpha = sorted(msg_given)
    sorted_list = sorted(msg_alpha, key=lambda c: msg_alpha.count(c))
    final_msg = "".join(sorted_list)
    return final_msg


t=int(input())
for _ in range(t):
    arr=list(map(int,input().split()))
    weight = []
    stack=[]
    letter = 'A'
    for i in range(arr[0]):
        ex = list(map(int,input().split()))
        for p in range(len(ex)):
            if len(stack)==0:
                stack.append(letter*ex[p])
                letter = chr(ord(letter)+1)
                print(stack)

