N1=int(input())
a1=list(map(int,input().split()))
c1=[]
count=0
for i1 in a1:
  if i1 not in c1:
    c1.append(i1)
for j1 in c1:
  for k1 in a1:
    if(j1==k1):
      count=count+1
  if(count==1):
    print(j1)
  count=0
