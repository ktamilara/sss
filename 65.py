number11,number12 = map(int,input().split())
number13 = list(map(int,input().split()))
amount1 = int(input())
total1 = (sum(number13)-number13[number12])//2
if amount1 == total1:
  print("Bon Appetit")
else:
  print(amount1-total1)
