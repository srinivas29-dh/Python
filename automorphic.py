n=int(input())
s=n*n
if str(s).endswith(str(n)):
   print("automorphic")
else:
   print("not automorphic")