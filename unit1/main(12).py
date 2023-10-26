def fact(n):
 if n==1:
   return n
 else:
   return n* fact(n-1)
num=7
if num<0:
  print("sorry,factorial does not exit for negative numbers")
elif num==0:
  print("the factorial for 0 is 1")
else:
  print("the factorial of",num,"is",fact(num))