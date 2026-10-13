a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
print("add/sub/multiple/div")
c=str(input("enter any one operation:"))
if(c=="add"):
  print(a+b)
elif(c=="sub"):
  print(a-b)
elif(c=="multiple"):
  print(a*b)
else:
  print(a/b)