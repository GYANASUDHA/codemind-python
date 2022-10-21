n=int(input())
z=n*n
sum=0
while z>0:
    r=z%10
    sum=sum+r
    z=z//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')