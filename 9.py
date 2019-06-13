n11=int(input())
l1=list(map(int,input().split()))
mi1=max(l1)
a1,b1=0,0
for i11 in range(0,len(l1)-1):
  for j1 in range(i1+1,len(l1)):
    if abs1(l[i]+l[j])<mi:
      a1,b1=l1[i1],l1[j1]
      mi1=abs1(a1+b1)
print(a1,b1)
