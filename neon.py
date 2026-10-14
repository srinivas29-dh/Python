n=int(input("enter the number:"))
m=n*n
sum=0
for i in str(m):
   sum+=int(i)
if sum==n:
   print("neon number")
else:
   print("not neon number")