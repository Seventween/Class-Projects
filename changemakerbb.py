import os
import random
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

TWENTY = 20.0
TEN = 10.0
FIVE = 5.0
DOLLAR = 1.0
QUART = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01
run = True
store = ["Apple Pie", "Socks", "Bird Seed"]
while run:
  print("\nWould you like to choose an item? If no, you may manually enter a price.")
  answer = input()
  if answer == "yes" or answer == "Yes":
    cls()
    for z in range(3):
      print(store[z])
    print("\nPlease enter your selection: ")
    choice = input()
    price = random.uniform(5.99,99.99)
    price = round(price,2)
    print("Your total today for your ", choice, " will be: ", price, ".\n")
    print("\nEnter tender amount: ")
    tender = input()
    tender = float(tender)
    tender = round(tender,2)
    subtotal = tender - price
    banger = subtotal
    banger = round(banger,2)
    subtotal = round(subtotal,2)
    subtotal = str(subtotal)
    x = subtotal.split(".")
    subint = x[0] + x[1]
    subint = int(subint)
    print("\n \nRemaining change: ", subint, "  ", banger)
    print("\n \nChange given: ")
    change = banger//TWENTY
    rema = banger%TWENTY
    rema = round(rema,2)
    print("Twenties: ", change, "\n")
    change = rema//TEN
    rema = rema%TEN
    print("Tens: ", change, "\n")
    change = rema//FIVE
    rema = rema%FIVE
    print("Fives: ", change, "\n")
    change = rema//DOLLAR
    rema = rema%DOLLAR
    print("Ones: ", change, "\n")
    change = rema//QUART
    rema = rema%QUART
    print("Quarters: ", change, "\n")
    change = rema//DIME
    rema = rema%DIME
    print("Dimes: ", change, "\n")
    change = rema//NICKLE
    rema = rema%NICKLE
    print("Nickles: ", change, "\n")
    change = rema//PENNY
    rema = rema%PENNY
    print("Pennies: ", change, "\n")
  else:
    print("\nPlease enter a purchase value: ")
    item = input()
    item = float(item)
    item = round(item,2)
    print("\n \n Enter tender amount: ")
    tender = input()
    tender = float(tender)
    tender = round(tender,2)
    subtotal = tender - item
    banger = subtotal
    banger = round(banger,2)
    subtotal = round(subtotal,2)
    subtotal = str(subtotal)
    x = subtotal.split(".")
    subint = x[0] + x[1]
    subint = int(subint)
    print("\n \nRemaining change: ", subint, "  ", banger)
    print("\n \nChange given: ")
    change = banger//TWENTY
    rema = banger%TWENTY
    rema = round(rema,2)
    print("Twenties: ", change, "\n")
    change = rema//TEN
    rema = rema%TEN
    print("Tens: ", change, "\n")
    change = rema//FIVE
    rema = rema%FIVE
    print("Fives: ", change, "\n")
    change = rema//DOLLAR
    rema = rema%DOLLAR
    print("Ones: ", change, "\n")
    change = rema//QUART
    rema = rema%QUART
    print("Quarters: ", change, "\n")
    change = rema//DIME
    rema = rema%DIME
    print("Dimes: ", change, "\n")
    change = rema//NICKLE
    rema = rema%NICKLE
    print("Nickles: ", change, "\n")
    change = rema//PENNY
    rema = rema%PENNY
    print("Pennies: ", change, "\n")
  print("Would you like to buy something else? ")
  answer = input()
  if answer == "Yes" or answer == "yes":
    cls()
    continue
  else:
    break
cls()
print("\n \n \nThank you for shopping with us!")