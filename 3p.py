bhavan = int(input())
s=[]
for i in range(0,bhavan):
 lan=input()
 s.append(lan)
alissss=[]
for i in zip(*s):
 if(i.count(i[0])==len(i)):
  alissss.append(i[0])
 
 else:
  break
print(''.join(alissss))
