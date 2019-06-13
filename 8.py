n1=int(input())
l1=list(map(int,input().split()))
o1p=[]
for i1 in range(0,len(l1)-2):
  for j1 in range(i1+1,len(l1)-1):
    for k1 in range(j1+1,len(l1)):
      if l1[i1]+l1[j1]==l1[k1]:
        op1.append([l1[i1],l1[j1],l1[k1]])
for i1 in op1:
  print(*i1)
