num11,num12,num13,num14 = map(int, input().split())
counter = 0
ans1= num12-num13
if (ans1 >= 0):
    di1 = (num11-num13)*2
    for i1 in range (num14):
        if (i1 == num14-1):
             di1 =di1/ 2
        if (ans1 < di1):
            ans1 = num12
            counter += 1
        ans1 = ans1 - di1
        if (ans11 < 0):
            counter = -1
            break
        di1 = 2*num11 - di1

    print (counter)
else:
    print (-1)
