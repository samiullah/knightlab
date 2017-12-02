import random
import math
random_number = random.randrange(1,100)


def guess(x):
  num = input(x)
  number = int(num)
  if number==random_number:
    print("Your guess was correct")
  elif(number is not random_number):
    diff = random_number - number
    difff = abs(diff)
    print("you lost by "+ str(difff))
    print("Actual number was " + str(random_number))


guess("Guess the number please:")





