from collections import *
a1 = int(input())
b1 = [int(i) for i in input().split(' ')]
d1 = defaultdict(int)

found = False
for i1 in range(a1):
    d1[b1[i1]] += 1
    if d1[b1[i1]] == 2:
        print(b1[i1])
        found = True
if not found:
    print("unique")
