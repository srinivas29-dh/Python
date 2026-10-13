a=int(input("enter the value:"))
if(a%3==0 & a%5==0):
  print("the number is divisible by 3 and 5")
elif(a%3==0):
  print("the number is divisible by 3")
elif(a%5==0):
  print("the number is divisible by 5")
else:
  print("the number not divisible by 3,5")