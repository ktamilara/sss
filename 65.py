num11,num12 = map(int,input().split())
num13 = list(map(int,input().split()))
amount1 = int(input())
total1 = (sum(num13)-num13[num12])//2
if amount1 == total1:
  print("Bon Appetit")
else:
  print(amount1-total1)
