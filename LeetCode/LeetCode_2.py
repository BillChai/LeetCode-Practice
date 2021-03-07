def AddTwo(l1,l2):
    length = len(l1)
    if len(l2)>len(l1):
        length = len(l2)
    
    answer = [0]*length

    for i in range(length):
        #answer.insert(i,(l1[i] + l2[i]+answer[i]))
        answer[i] = l1[i] + l2[i] + answer[i]
        print(answer)
        if answer[i]>=10:
            #del answer[i]
            answer[i] = (l1[i] + l2[i])%10
            if(i==length-1):
                answer.append(1)
            else:
                answer[i+1] = 1

    print(answer)

l1 = [2,4,3]
l2 = [5,6,4]

AddTwo(l1,l2)