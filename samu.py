from itertools import combinations
so,t=input().split()
t=int(t)
top=[]
va=len(so)-t
fake=combinations(so,va)
for i in list(fake):
  top.append("".join(i))
print(min(top))
