from replit import clear

my_dict={}



while True:
  name=input("whats your name")
  bid=int(input("whats your bid"))
  my_dict[name]=bid
  choice=input("any one else for bid--> yes/no")
  clear()
  if choice=="no":
    break

winner=0


for key in my_dict:
  if my_dict[key]>winner:
    winner=my_dict[key])
    a=key

print(f"Winner of this bid is {a} with bid of {winner}")
