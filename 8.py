n11=int(input())
li1=list(map(int,input().split()))
op1=[]
for i1 in range(0,len(li1)-2):
  for j1 in range(i1+1,len(li1)-1):
    for k1 in range(j1+1,len(li1)):
      if li1[i1]+li1[j1]==li1[k1]:
        op.append([li1[i1],li1[j1],li1[k1]])
for i1 in op1:
  print(*i1)
