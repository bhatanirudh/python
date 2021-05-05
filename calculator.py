def add(n1,n2):
  return n1+n2 

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2 
flag=0
while flag==0:

 a=float(input("Enter first number"))
 b=float(input("Enter second number"))
 choice=input("Enter operation +, - , / , X ")
 my_dict={
  "+":add,
  "-":sub,
  "X":mul,
  "/":div
 }
 for symbol in my_dict:
   if choice==symbol:
     function=my_dict[symbol]
     print(function(a,b))
 c=input("do you want to continue?y/n")
 if c=="n":
   flag=1 
