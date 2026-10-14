n=int(input("enter a number"))
if n%1==0 and n%n==0:
 if n%2!=0 or n==2:
  print("prime number")
else:
  print("not prime number")