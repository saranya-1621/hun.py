m, n = map(int,input().split())
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))
flag = 1
for i in l3:
    if i not in l2:
        print('NO')
        flag = 0
        break
if(flag):
    print('YES')
