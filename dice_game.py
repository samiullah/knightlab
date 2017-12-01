import random
dice=random.randrange(1,6)
print(dice)

if(dice>0):
  x=input("do u wana roll again: Enter yes or no")
  if(x=="yes"):
    dice=random.randrange(1,6)
    print(dice)
  elif(x=="no"):
    print("Bye bye Thanks for playing")
