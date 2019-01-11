n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(0,len(l)):
   sum=sum+l[i]
avg=sum//n
#print result
print(avg)
