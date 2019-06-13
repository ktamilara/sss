b1=int(input())
sb1=str(b1)
q1=0
for i1 in range(0,len(sb1)):
    if int(sb1[i1:i1+2])<26 and len(str(int(sb1[i1:i1+2])))==2:
        q1+=1
if q1==2:
    print(q1+q1//2)
else:
    print(q1+q1//2+1)
