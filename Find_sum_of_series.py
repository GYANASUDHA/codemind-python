num=int(input())
sum=0
for i in range(1,num+1,+1):
    a=1/i
    sum+=a
print('{:.2f}'.format(sum))