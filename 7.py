l1=int(input())
arr1=list(map(int,input().split()))
for i1 in range(0,len(arr1)):
    if(arr1[i1]%2==0 and i1%2!=0):
        print(arr1[i1],end=" ")
    elif(arr[i1]%2!=0 and i1%2==0):
        print(ar1r[i1],end=" ")
