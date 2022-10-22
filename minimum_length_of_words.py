n=input()
a=n.split()
c=111111
for i in a:
    d=len(i)
    if d<c:
        c=d
print(c)