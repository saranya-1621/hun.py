sadevi=list(input())
for i in range(0,len(sadevi),2):
   sadevi[i],sadevi[i+1]=sadevi[i+1],sadevi[i]
pri=''.join(sadevi)
print(pri)
