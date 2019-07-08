aasan,aauma=map(str,input().split())
if(len(aasan)!=len(aauma)):
    print("no")
else :
    s2=[aasan.count(i) for i in aasan]
    s3=[aauma.count(i) for i in aauma]
if(s2==s3):
    print("yes")
else:
    print("no")
