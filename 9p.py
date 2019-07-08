ccha,ccho=map(int,input().split())
csaa=[]
for p in range(ccha+1,ccho+1):
  if p>1:
    for f in range(2,p):
      if(p%f==0):
        break
    else:
      csaa.append(f)
print(len(csaa)+1)
