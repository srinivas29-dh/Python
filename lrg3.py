a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
c=int(input("enter the number 3:"))
if(a>b and a>c):
  print("the largest number is:",a)
elif(b>c):
  print("the largest number is:",b)
else:
  print("the largest number is:",c)